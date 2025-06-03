import pandas as pd
import streamlit as st


def timeline_select_slider(superstore_data: pd.DataFrame) -> pd.DataFrame:
    order_date = superstore_data["Order Date"]

    all_dates = order_date.dt.year.drop_duplicates().sort_values().to_list()

    start_date, end_date = st.sidebar.select_slider(
        label="Select a start and end date:",
        options=all_dates,
        value=(all_dates[0], all_dates[-1]),
    )

    start_date, end_date = (
        pd.to_datetime(start_date),
        pd.to_datetime(end_date),
    )

    order_date_mask = (order_date >= start_date) & (order_date <= end_date)

    return superstore_data[order_date_mask]
