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
APP_DIR = Path(__file__).parent
PRJ_PATH = APP_DIR.parent
DATA_PATH = PRJ_PATH /Path("data/licenses.xlsx")

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
    
    # Filter for granted licenses as per PRD
    if "status" in df.columns:
        df = df[df["status"].str.lower() == "granted"]
    
    # Ensure zipcode is treated as a string for categorical plotting
    if "zipcode" in df.columns:
        df["zipcode"] = df["zipcode"].astype(str).str.replace(".0", "", regex=False)
        
    return df

def main():
    st.title("🍹 Boston Licensing Board Dashboard")
    st.markdown("Analyzing granted licenses by Zipcode and Alcohol Type.")

    df = load_data()

    if df.empty:
        st.warning("No data available to display.")
        return

    # Sidebar Filters
    st.sidebar.header("Filters")
    
    # Date Range Filter
    if "minutes_date" in df.columns:
        min_date = df["minutes_date"].min().date()
        max_date = df["minutes_date"].max().date()
        
        start_date, end_date = st.sidebar.date_input(
            "Select Date Range",
            value=(min_date, max_date),
            min_value=min_date,
            max_value=max_date
        )
        
        # Apply date filter
        mask = (df["minutes_date"].dt.date >= start_date) & (df["minutes_date"].dt.date <= end_date)
        filtered_df = df[mask]
    else:
        filtered_df = df

    # Display Metrics
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Licenses (Granted)", len(filtered_df))
    col2.metric("Unique Zipcodes", filtered_df["zipcode"].nunique() if "zipcode" in filtered_df.columns else 0)
    col3.metric("Alcohol Types", filtered_df["alcohol_type"].nunique() if "alcohol_type" in filtered_df.columns else 0)

    # Main Visual: Stacked Bar Chart
    st.subheader("Licenses by Zipcode and Alcohol Type")
    
    if "zipcode" in filtered_df.columns and "alcohol_type" in filtered_df.columns:
        # Group data for the chart
        chart_data = filtered_df.groupby(["zipcode", "alcohol_type"]).size().reset_index(name="count")
        
        # Create stacked bar chart using streamlit's native bar_chart
        # We pivot to get zipcodes as index and alcohol types as columns
        pivot_df = chart_data.pivot(index="zipcode", columns="alcohol_type", values="count").fillna(0)
        
        st.bar_chart(pivot_df, use_container_width=True)
    else:
        st.error("Required columns ('zipcode', 'alcohol_type') missing from data.")

    # Data Table View
    with st.expander("View Filtered Data"):
        st.dataframe(filtered_df)

if __name__ == "__main__":
    main()
