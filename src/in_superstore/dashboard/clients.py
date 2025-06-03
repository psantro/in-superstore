import pandas as pd
import streamlit as st


def clients() -> None:
    superstore_data = st.session_state.get("superstore_data", pd.DataFrame())

    st.title("Clientes")

    col1, col2, col3 = st.columns(3)

    n_customers = superstore_data["Customer ID"].nunique()
    n_orders = superstore_data["Order ID"].nunique()
    avg_sales_per_customer = (
        superstore_data.groupby("Customer ID", observed=False)["Sales"].sum().mean()
    )
    repeat_customers = (
        superstore_data.groupby("Customer ID", observed=False)["Order ID"].nunique().gt(1).sum()
    )

    col1.metric("Clientes únicos", f"{n_customers}")
    col2.metric("Pedidos únicos", f"{n_orders}")
    col3.metric("Pedidos por cliente", f"{n_orders / n_customers:.2f}")

    col1.metric("Venta media por cliente", f"${avg_sales_per_customer:,.2f}")
    col2.metric("Clientes recurrentes", f"{repeat_customers}")
    col3.metric("Porcentaje recurrentes", f"{(repeat_customers / n_customers) * 100:.1f}%")

    st.subheader("Clientes únicos por año")
    superstore_data["Order Date"] = pd.to_datetime(superstore_data["Order Date"])
    customers_year = (
        superstore_data.groupby(superstore_data["Order Date"].dt.year)["Customer ID"]
        .nunique()
        .reset_index()
    )
    customers_year.columns = ["Año", "Clientes únicos"]
    customers_year["Year"] = customers_year["Year"].astype(str)
    st.line_chart(customers_year.set_index("Year"))
