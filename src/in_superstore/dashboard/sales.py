import pandas as pd
import streamlit as st


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

    tab1, tab2 = st.tabs(["General", "Geographic"])

    with tab1:
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
            delta_color=(
                "normal" if total_sales_last >= total_sales_prev else "inverse"
            ),
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
            delta_color=(
                "normal" if total_profit_last >= total_profit_prev else "inverse"
            ),
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

        yearly_orders = (
            superstore_data.groupby("Year")["Order ID"].nunique().reset_index()
        )
        yearly_orders["Year"] = yearly_orders["Year"].astype(str)
        yearly_orders.columns = ["Year", "Count"]

        st.line_chart(
            yearly_orders,
            x="Year",
            y="Count",
            use_container_width=True,
        )

    with tab2:
        st.subheader("Geographic Sales")

        pc_sales = (
            superstore_data.groupby("Postal Code", observed=False)
            .size()
            .reset_index(name="Ventas")
        )

        geo_sales = pc_sales.merge(
            geographic_data,
            left_on="Postal Code",
            right_on="postal_code",
            how="left",
        )

        geo_sales = geo_sales.dropna(
            subset=["latitude", "longitude"],
        )

        geo_sales["Ventas"] = geo_sales["Ventas"] * 250

        st.map(geo_sales, size="Ventas")

        st.subheader("States Sales")
        city_sales = (
            superstore_data.groupby("State", observed=False)
            .size()
            .reset_index(name="Ventas")
            .sort_values("Ventas", ascending=False)
            .head(20)
        )
        st.bar_chart(
            city_sales.set_index("State"),
            use_container_width=True,
        )
