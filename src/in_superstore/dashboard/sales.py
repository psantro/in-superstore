import pandas as pd
import streamlit as st
from statsmodels.tsa.arima.model import ARIMA


def show_general_tab(superstore_data):
    st.subheader("General KPIs")
    last_year = superstore_data["Year"].max()
    prev_year = last_year - 1

    df_last = superstore_data[superstore_data["Year"] == last_year]
    df_prev = superstore_data[superstore_data["Year"] == prev_year]

    total_sales_last = df_last["Sales"].sum()
    total_sales_prev = df_prev["Sales"].sum()
    total_profit_last = df_last["Profit"].sum()
    total_profit_prev = df_prev["Profit"].sum()
    n_orders_last = df_last["Order ID"].nunique()
    n_orders_prev = df_prev["Order ID"].nunique()

    col1, col2, col3 = st.columns(3)
    col1.metric(
        "Sales count (last year)",
        f"{n_orders_last}",
        delta=(
            f"{n_orders_last - n_orders_prev} "
            f"({((n_orders_last - n_orders_prev) / n_orders_prev * 100):.2f}%)"
            if n_orders_prev
            else "N/A"
        ),
        delta_color=("normal" if n_orders_last >= n_orders_prev else "inverse"),
    )
    col2.metric(
        "Total amount sales (last year)",
        f"${total_sales_last:,.0f}",
        delta=(
            f"${total_sales_last - total_sales_prev:,.0f} "
            f"({((total_sales_last - total_sales_prev) / total_sales_prev * 100):.2f}%)"
            if total_sales_prev
            else "N/A"
        ),
        delta_color=("normal" if total_sales_last >= total_sales_prev else "inverse"),
    )
    col3.metric(
        "Total profit (last year)",
        f"${total_profit_last:,.0f}",
        delta=(
            f"${total_profit_last - total_profit_prev:,.0f} "
            f"({((total_profit_last - total_profit_prev) / total_profit_prev * 100):.2f}%)"
            if total_profit_prev
            else "N/A"
        ),
        delta_color=("normal" if total_profit_last >= total_profit_prev else "inverse"),
    )

    st.subheader("Profit per year")
    yearly_profit = superstore_data.groupby("Year")["Profit"].sum().reset_index()
    yearly_profit["Year"] = yearly_profit["Year"].astype(str)
    st.line_chart(
        yearly_profit,
        x="Year",
        y="Profit",
        use_container_width=True,
    )

    st.subheader("Orders per year")
    yearly_orders = superstore_data.groupby("Year")["Order ID"].nunique().reset_index()
    yearly_orders["Year"] = yearly_orders["Year"].astype(str)
    yearly_orders.columns = ["Year", "Count"]
    st.line_chart(
        yearly_orders,
        x="Year",
        y="Count",
        use_container_width=True,
    )


def show_geographic_tab(superstore_data, geographic_data):
    st.subheader("Geographic Sales")
    pc_sales = (
        superstore_data.groupby("Postal Code", observed=False)
        .size()
        .reset_index(name="Sales")
    )
    geo_sales = pc_sales.merge(
        geographic_data,
        left_on="Postal Code",
        right_index=True,
        how="left",
    )
    geo_sales = geo_sales.dropna(
        subset=["Latitude", "Longitude"],
    )
    geo_sales["Sales"] = geo_sales["Sales"] * 250
    st.map(geo_sales, size="Sales", latitude="Latitude", longitude="Longitude")

    st.subheader("Sales and profit by region")
    region_df = (
        superstore_data.groupby("Region", observed=False)
        .agg({"Sales": "sum", "Profit": "sum"})
        .reset_index()
    )
    region_df = region_df.sort_values("Sales", ascending=False)
    st.dataframe(
        region_df.style.format({"Sales": "${:,.2f}", "Profit": "${:,.2f}"}),
        use_container_width=True,
        hide_index=True,
    )
    st.subheader("Sales by region (bar charts)")
    st.bar_chart(
        region_df.set_index("Region")["Sales"],
        use_container_width=True,
    )


def show_predictions_tab(superstore_data):
    st.subheader("Sales Predictions")

    orders_monthly = (
        superstore_data.set_index("Order Date")
        .resample("ME")["Order ID"]
        .nunique()
        .reset_index()
    )
    orders_monthly.columns = ["Month", "Orders"]

    model_orders = ARIMA(orders_monthly["Orders"], order=(1, 1, 1))
    model_orders_fit = model_orders.fit()
    forecast_orders = model_orders_fit.forecast(steps=1)
    next_month_orders = int(round(forecast_orders.iloc[0]))

    st.metric("Predicted number of orders next month", f"{next_month_orders}")

    orders_monthly_forecast = orders_monthly.copy()
    next_month = orders_monthly["Month"].max() + pd.offsets.MonthBegin(1)
    orders_monthly_forecast = pd.concat(
        [
            orders_monthly_forecast,
            pd.DataFrame({"Month": [next_month], "Orders": [forecast_orders.iloc[0]]}),
        ],
        ignore_index=True,
    )
    orders_monthly_forecast["Month"] = orders_monthly_forecast["Month"].dt.strftime(
        "%Y-%m"
    )
    orders_monthly_forecast_tail = orders_monthly_forecast.tail(13)
    st.line_chart(
        orders_monthly_forecast_tail.set_index("Month"),
        use_container_width=True,
    )
    profit_monthly = (
        superstore_data.set_index("Order Date")
        .resample("ME")["Profit"]
        .sum()
        .reset_index()
    )
    profit_monthly.columns = ["Month", "Profit"]

    model_profit = ARIMA(profit_monthly["Profit"], order=(1, 1, 1))
    model_profit_fit = model_profit.fit()
    forecast_profit = model_profit_fit.forecast(steps=1)
    next_month_profit = forecast_profit.iloc[0]

    st.metric("Predicted profit next month", f"${next_month_profit:,.2f}")

    profit_monthly_forecast = profit_monthly.copy()
    profit_monthly_forecast = pd.concat(
        [
            profit_monthly_forecast,
            pd.DataFrame({"Month": [next_month], "Profit": [forecast_profit.iloc[0]]}),
        ],
        ignore_index=True,
    )
    profit_monthly_forecast["Month"] = profit_monthly_forecast["Month"].dt.strftime(
        "%Y-%m"
    )
    profit_monthly_forecast_tail = profit_monthly_forecast.tail(13)
    st.line_chart(
        profit_monthly_forecast_tail.set_index("Month"),
        use_container_width=True,
    )


def sales() -> None:
    superstore_data = st.session_state.get(
        "superstore_data",
        pd.DataFrame(),
    )
    geographic_data = st.session_state.get(
        "geographic_data",
        pd.DataFrame(),
    )

    st.title("📊 Sales 🛒")

    superstore_data["Order Date"] = pd.to_datetime(
        superstore_data["Order Date"],
    )
    superstore_data["Year"] = superstore_data["Order Date"].dt.year

    tab1, tab2, tab3 = st.tabs(["General", "Geographic", "Predictions"])

    with tab1:
        show_general_tab(superstore_data)
    with tab2:
        show_geographic_tab(superstore_data, geographic_data)
    with tab3:
        show_predictions_tab(superstore_data)
