import streamlit as st
import pandas as pd
from pathlib import Path

# Set page configuration
st.set_page_config(
    page_title="Boston Licensing Board Dashboard",
    page_icon="🍹",
    layout="wide"
)

# Constants
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "licenses.xlsx"

TARGETED_ZIPCODES = ["02126", "02121", "02119", "02124", "02136", "02125", "02122", "02118", "02128", "02131", "02130", "02129", "02132"]
NON_TARGETED_ZIPCODES = ["02111", "02120", "02134", "02115", "02199", "02215", "02116", "02114", "02127", "02108", "02210", "02109", "02113", "02110", "02128"]

@st.cache_data
def load_data():
    """Load and preprocess the licensing data."""
    if not DATA_PATH.exists():
        st.error(f"Data file not found at {DATA_PATH.absolute()}")
        return pd.DataFrame()
    
    df = pd.read_excel(DATA_PATH)
    
    # Convert minutes_date to datetime if it exists
    if "minutes_date" in df.columns:
        df["minutes_date"] = pd.to_datetime(df["minutes_date"])
        
    # Ensure zipcode is treated as a 5-digit string for categorical plotting and filtering
    if "zipcode" in df.columns:
        # Convert to string, remove potential .0, and pad to 5 digits
        df["zipcode"] = (
            df["zipcode"]
            .astype(str)
            .str.replace(".0", "", regex=False)
            .str.zfill(5)
        )
        
    return df

def render_download_section():
    """Render the data download button."""
    if DATA_PATH.exists():
        with open(DATA_PATH, "rb") as f:
            st.download_button(
                label="📥 Download Full Dataset (Excel)",
                data=f,
                file_name="licenses.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
    else:
        st.warning("Excel file not available for download.")

def render_business_search(df):
    """Render the business search section."""
    st.header("Business Search")
    st.caption(f"Searching {len(df):,} total records")

    # Radio button to select search mode
    search_mode = st.radio(
        "Search Mode",
        options=["Business Name", "License Number"],
        horizontal=True
    )

    # Multi-line text area for input
    if search_mode == "Business Name":
        placeholder_text = "Enter business names (one per line)\ne.g.\nStarbucks\nThe Ginger Man\nNicole's Pizza"
        search_label = "Business Names"
    else:
        placeholder_text = "Enter license numbers (one per line)\ne.g.\nLB-123456\nLB-789012\nLB-345678"
        search_label = "License Numbers"

    search_input = st.text_area(
        search_label,
        placeholder=placeholder_text,
        height=150
    )

    if search_input.strip():
        # Parse input - split by newlines and clean up
        search_terms = [term.strip() for term in search_input.split('\n') if term.strip()]
        
        if not search_terms:
            st.info(f"Please enter at least one {search_label.lower()}.")
            st.divider()
            return
        
        # Track found and not found
        found_results = []
        not_found = []
        
        if search_mode == "Business Name":
            # Search in business_name and dba_name columns
            search_cols = ["business_name", "dba_name"]
            cols_to_search = [c for c in search_cols if c in df.columns]
            
            if not cols_to_search:
                st.error("Business name columns not found in data.")
                st.divider()
                return
            
            for term in search_terms:
                # Search for this term (case-insensitive)
                term_lower = term.lower()
                matches = df[df[cols_to_search].apply(
                    lambda x: x.astype(str).str.lower().str.contains(term_lower, na=False, regex=False)
                ).any(axis=1)]
                
                if not matches.empty:
                    # Add all matches for this term
                    for _, row in matches.iterrows():
                        found_results.append(row)
                else:
                    not_found.append(term)
        
        else:  # License Number mode
            if "license_number" not in df.columns:
                st.error("License number column not found in data.")
                st.divider()
                return
            
            for term in search_terms:
                # Search for exact license number (case-insensitive)
                matches = df[df["license_number"].astype(str).str.lower() == term.lower()]
                
                if not matches.empty:
                    found_results.append(matches.iloc[0])
                else:
                    not_found.append(term)
        
        # Display not found entries
        if not_found:
            st.warning(f"**Not Found ({len(not_found)}):** {', '.join(not_found)}")
        
        # Display found results
        if found_results:
            st.success(f"**Found {len(found_results)} record(s)**")
            
            # Convert to dataframe
            found_df = pd.DataFrame(found_results)
            
            # Remove duplicates if any
            found_df = found_df.drop_duplicates()
            
            # Hide specific columns for the table view
            hide_cols = ["address", "state", "status_detail", "entity_number"]
            display_cols = [c for c in found_df.columns if c not in hide_cols]
            
            # Display as an interactive table
            event = st.dataframe(
                found_df[display_cols],
                use_container_width=True,
                on_select="rerun",
                selection_mode="single-row",
                hide_index=True
            )
            
            # Show Details if selected
            if event.selection.rows:
                selected_row_idx = event.selection.rows[0]
                selected_row = found_df.iloc[selected_row_idx]
                
                st.markdown("### License Details")
                details = selected_row.dropna().to_dict()
                st.json(details)
        else:
            st.info("No records found.")
    else:
        st.info(f"Enter {search_label.lower()} above to begin search.")

    st.divider()


def filter_by_date(chart_df):
    """Filter the dataframe by date using a slider."""
    if "minutes_date" in chart_df.columns:
        # Get unique sorted meeting dates
        available_dates = sorted(chart_df["minutes_date"].dropna().unique())
        
        # Convert to string format for the slider (YYYY-MM-DD)
        date_options = [pd.to_datetime(d).strftime('%Y-%m-%d') for d in available_dates]
        
        if not date_options:
             st.warning("No valid meeting dates found.")
             return chart_df
        
        # Default to full range
        start_default = date_options[0]
        end_default = date_options[-1]

        selected_range = st.select_slider(
            "Select Meeting Range",
            options=date_options,
            value=(start_default, end_default)
        )
        
        start_date_str, end_date_str = selected_range
        
        # Convert back to datetime for filtering
        start_date = pd.to_datetime(start_date_str)
        end_date = pd.to_datetime(end_date_str)
        
        # Filter for Charts
        mask = (chart_df["minutes_date"] >= start_date) & (chart_df["minutes_date"] <= end_date)
        return chart_df[mask]
    else:
        return chart_df

def render_metrics(charts_df):
    """Render summary metrics."""
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Licenses (Granted)", len(charts_df))
    col2.metric("Unique Zipcodes", charts_df["zipcode"].nunique() if "zipcode" in charts_df.columns else 0)
    col3.metric("Alcohol Types", charts_df["alcohol_type"].nunique() if "alcohol_type" in charts_df.columns else 0)

def render_zipcode_charts(charts_df):
    """Render targeted and non-targeted zipcode charts."""
    if "zipcode" in charts_df.columns and "alcohol_type" in charts_df.columns:
        
        # 1. Targeted Zipcodes Chart
        st.subheader("Targeted Zipcodes")
        targeted_df = charts_df[charts_df["zipcode"].isin(TARGETED_ZIPCODES)]
        if not targeted_df.empty:
            chart_data_targeted = targeted_df.groupby(["zipcode", "alcohol_type"]).size().reset_index(name="count")
            pivot_df_targeted = chart_data_targeted.pivot(index="zipcode", columns="alcohol_type", values="count").fillna(0)
            st.bar_chart(pivot_df_targeted, use_container_width=True)
        else:
            st.info("No data available for Targeted Zipcodes in the selected range.")

        # 2. Non-Targeted Zipcodes Chart
        st.subheader("Non-Targeted Zipcodes")
        non_targeted_df = charts_df[charts_df["zipcode"].isin(NON_TARGETED_ZIPCODES)]
        if not non_targeted_df.empty:
            chart_data_non_targeted = non_targeted_df.groupby(["zipcode", "alcohol_type"]).size().reset_index(name="count")
            pivot_df_non_targeted = chart_data_non_targeted.pivot(index="zipcode", columns="alcohol_type", values="count").fillna(0)
            st.bar_chart(pivot_df_non_targeted, use_container_width=True)
        else:
            st.info("No data available for Non-Targeted Zipcodes in the selected range.")
            
    else:
        st.error("Required columns ('zipcode', 'alcohol_type') missing from data.")

    st.divider()

def render_meeting_chart(charts_df):
    """Render the Granted Licenses by Meeting chart."""
    st.subheader("Granted Licenses by meeting")
    
    if "minutes_date" in charts_df.columns:
        # Group by meeting date and count
        meeting_counts = charts_df.groupby("minutes_date").size().reset_index(name="Granted Licenses")
        # Set index to minutes_date for the bar chart
        meeting_counts = meeting_counts.set_index("minutes_date")
        
        st.bar_chart(meeting_counts, y="Granted Licenses", use_container_width=True)
    else:
        st.info("No meeting date information available.")

    st.divider()

def render_analysis_section(df):
    """Render the analysis section with date filtering and charts."""
    st.header("Analyzing Granted Licenses")
    
    if "status" in df.columns:
        chart_df = df[
            df["status"]
            .str.lower()
            .isin(["granted", "active"])
        ]
    else:
        chart_df = df 

    if chart_df.empty:
        st.warning("No data available to display.")
        return

    # Filter by Date
    charts_df = filter_by_date(chart_df)

    # Display Metrics
    render_metrics(charts_df)

    # Render Charts
    render_zipcode_charts(charts_df)
    render_meeting_chart(charts_df)

def main():
    st.title("🍹 Boston Licensing Board Dashboard")
    render_download_section()

    df = load_data()

    render_business_search(df)
    render_analysis_section(df)
 

if __name__ == "__main__":
    main()
