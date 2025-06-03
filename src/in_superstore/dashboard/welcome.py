import pandas as pd
import streamlit as st


def welcome() -> None:
    st.title("👔 Executive Dashboard 💼")

    st.markdown(
        """
    ## Welcome to the Executive Dashboard
    This dashboard provides an overview of the American Superstore data, focusing on key performance indicators (KPIs) for sales, products and clients.

    ### Sections:
    - **Sales**: Explore sales trends, performance by region, and key metrics.
    - **Products**: Analyze product performance, including best-sellers and profit margins.
    - **Clients**: Understand client demographics, purchasing behavior, and loyalty metrics.

    Use the sidebar to navigate between sections and explore the data in detail.
    """,
    )

    st.subheader("Data Overview")

    superstore_data = st.session_state.get("superstore_data", pd.DataFrame())
    geo_data = st.session_state.get("geographic_data", pd.DataFrame())

    st.dataframe(superstore_data)
    st.dataframe(geo_data)
