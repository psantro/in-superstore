import pandas as pd
import plotly.express as px
import streamlit as st


def customers() -> None:
    superstore_data = st.session_state.get("superstore_data", pd.DataFrame())

    st.title("🧍‍♂️ Customers 🧍‍♀️")

    col1, col2, col3 = st.columns(3)

    n_customers = superstore_data["Customer ID"].nunique()
    n_orders = superstore_data["Order ID"].nunique()
    avg_sales_per_customer = (
        superstore_data.groupby("Customer ID", observed=False)["Sales"].sum().mean()
    )
    repeat_customers = (
        superstore_data.groupby("Customer ID", observed=False)["Order ID"]
        .nunique()
        .gt(1)
        .sum()
    )

    col1.metric("Unique customers", f"{n_customers}")
    col2.metric("Unique orders", f"{n_orders}")
    col3.metric("Orders per customer", f"{n_orders / n_customers:.2f}")

    col1.metric("Average sales per customer", f"${avg_sales_per_customer:,.2f}")
    col2.metric("Repeat customers", f"{repeat_customers}")
    col3.metric("Repeat customer %", f"{(repeat_customers / n_customers) * 100:.1f}%")

    st.subheader("Unique customers per year")
    superstore_data["Order Date"] = pd.to_datetime(superstore_data["Order Date"])
    customers_year = (
        superstore_data.groupby(superstore_data["Order Date"].dt.year)["Customer ID"]
        .nunique()
        .reset_index()
    )
    customers_year.columns = ["Year", "Unique customers"]
    customers_year["Year"] = customers_year["Year"].astype(str)
    st.line_chart(customers_year.set_index("Year"), use_container_width=True)

    st.subheader("Customer segments")

    segment_counts = (
        superstore_data.groupby("Segment", observed=False)["Customer ID"]
        .nunique()
        .reset_index()
    )
    segment_counts.columns = ["Segment", "Unique customers"]

    fig_segment = px.pie(
        segment_counts,
        names="Segment",
        values="Unique customers",
        title="Customer segment proportion",
    )
    st.plotly_chart(fig_segment, use_container_width=True)
