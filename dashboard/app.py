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
<<<<<<< HEAD
APP_DIR = Path(__file__).parent
PRJ_PATH = APP_DIR.parent
DATA_PATH = PRJ_PATH /Path("data/licenses.xlsx")
=======
DATA_PATH = Path("../data/licenses.xlsx")
TARGETED_ZIPCODES = ["02126", "02121", "02119", "02124", "02136", "02125", "02122", "02118", "02128", "02131", "02130", "02129", "02132"]
NON_TARGETED_ZIPCODES = ["02111", "02120", "02134", "02115", "02199", "02215", "02116", "02114", "02127", "02108", "02210", "02109", "02113", "02110", "02128"]
>>>>>>> 1033cf9 (update dashboard)

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

def main():
    st.title("🍹 Boston Licensing Board Dashboard")
 
    # Download Excel file
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


    df = load_data()

    # --- Section 1: Business Search (Independent) ---
    st.header("Business Search")
    st.caption(f"Searching {len(df):,} total records")

    search_query = st.text_input("Search by Name, DBA, or License #", placeholder="e.g. Starbucks").strip().lower()

    if search_query:
        # Search logic on the FULL dataset (df), independent of date range
        search_cols = ["business_name", "dba_name", "license_number"]
        cols_to_search = [c for c in search_cols if c in df.columns]
        
        if cols_to_search:
            search_mask = df[cols_to_search].apply(
                lambda x: x.astype(str).str.lower().str.contains(search_query, na=False)
            ).any(axis=1)
            search_results = df[search_mask]
        else:
            search_results = pd.DataFrame()

        st.write(f"Found {len(search_results)} results:")
        
        # Hide specific columns for the table view
        #hide_cols = ["address", "state", "status_detail", "details", "entity_number"]
        hide_cols = ["address", "state", "status_detail", "entity_number"]
        display_cols = [c for c in search_results.columns if c not in hide_cols]

        # Interactive Table with Selection
        # We use st.dataframe with on_select
        event = st.dataframe(
            search_results[display_cols],
            use_container_width=True,
            on_select="rerun",
            selection_mode="single-row",
            hide_index=True
        )
        
        # Show Details if selected
        if event.selection.rows:
            selected_row_idx = event.selection.rows[0]
            # Get the actual row from the filtered dataframe using iloc
            selected_row = search_results.iloc[selected_row_idx]
            
            st.markdown("### License Details")
            # Display details in a nice format (e.g., JSON or key-value pairs)
            # Filter out internal columns/NaNs for cleaner view
            details = selected_row.dropna().to_dict()
            st.json(details)
    else:
        st.info("Enter a search term to find businesses.")

    st.divider()

    # --- Section 1: Charts & Analysis (Controlled by Date) ---
    st.header("Analyzing Granted Licenses")

    # Filter for granted licenses as per PRD
    if "status" in df.columns:
        chart_df = df[df["status"].str.lower() == "granted"]

    if chart_df.empty:
        st.warning("No data available to display.")
        return

    # Quarterly Range Slider (Full Width)
    if "minutes_date" in chart_df.columns:
        # Get all quarters in the data range
        min_date = chart_df["minutes_date"].min()
        max_date = chart_df["minutes_date"].max()
        
        # Simpler approach: construct quarterly labels
        all_quarters = pd.date_range(start=min_date, end=max_date, freq='QS')
        if not all_quarters.empty and all_quarters[0] > min_date:
             all_quarters = all_quarters.insert(0, min_date.to_period('Q').start_time)
        if all_quarters.empty or all_quarters[-1] < max_date:
            all_quarters = all_quarters.insert(len(all_quarters), max_date.to_period('Q').start_time)

        all_quarters = sorted(list(set(all_quarters)))
        labels = [f"Q{q.quarter} {q.year}" for q in all_quarters]
        label_to_date = dict(zip(labels, all_quarters))

        selected_range = st.select_slider(
            "Select Quarter Range",
            options=labels,
            value=(labels[0], labels[-1])
        )
        
        start_label, end_label = selected_range
        start_date = label_to_date[start_label]
        end_date = label_to_date[end_label] + pd.offsets.QuarterEnd(0)
        
        # Filter for Charts
        mask = (chart_df["minutes_date"] >= start_date) & (chart_df["minutes_date"] <= end_date)
        charts_df = chart_df[mask]
    else:
        charts_df = chart_df

    # Display Metrics
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Licenses (Granted)", len(charts_df))
    col2.metric("Unique Zipcodes", charts_df["zipcode"].nunique() if "zipcode" in charts_df.columns else 0)
    col3.metric("Alcohol Types", charts_df["alcohol_type"].nunique() if "alcohol_type" in charts_df.columns else 0)

    # Charts Section
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


if __name__ == "__main__":
    main()
