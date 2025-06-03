import pandas as pd
import plotly.express as px
import streamlit as st


def products() -> None:
    superstore_data = st.session_state.get("superstore_data", pd.DataFrame())

    n_products = superstore_data["Product Name"].nunique()
    n_categories = superstore_data["Category"].nunique()
    n_subcategories = superstore_data["Sub-Category"].nunique()

    st.title("🛍️ Products 📦")

    col1, col2, col3 = st.columns(3)
    col1.metric("Productos únicos", n_products)
    col2.metric("Categorías", n_categories)
    col3.metric("Subcategorías", n_subcategories)

    st.subheader("Productos más vendidos")

    top_products = (
        superstore_data.groupby("Product Name", observed=False)["Quantity"]
        .sum()
        .sort_values(ascending=False)
    )
    top_products = top_products.reset_index()
    top_products.columns = ["Nombre del producto", "Ventas"]
    st.dataframe(top_products, use_container_width=True, hide_index=True)

    st.subheader("Productos que reportan más beneficio")

    margin_products = (
        superstore_data.groupby("Product Name", observed=False)["Profit"]
        .sum()
        .sort_values(ascending=False)
    )
    margin_products = margin_products.reset_index()
    margin_products.columns = ["Nombre del producto", "Beneficio"]
    st.dataframe(
        margin_products.style.format(
            {
                "Beneficio": "${:,.2f}",
            }
        ),
        use_container_width=True,
        hide_index=True,
    )

    st.subheader("Distribución de ventas por categoría")
    category_sales = (
        superstore_data.groupby("Category", observed=False)["Order ID"]
        .nunique()
        .reset_index()
    )
    category_sales.columns = ["Category", "Count"]
    fig_cat = px.pie(
        category_sales, names="Category", values="Count", title="Ventas por categoría"
    )
    st.plotly_chart(fig_cat, use_container_width=True)

    st.subheader("Distribución de ventas por subcategoría")
    subcategory_sales = (
        superstore_data.groupby("Sub-Category", observed=False)["Order ID"]
        .nunique()
        .reset_index()
    )
    subcategory_sales.columns = ["Sub-Category", "Count"]
    fig_subcat = px.pie(
        subcategory_sales,
        names="Sub-Category",
        values="Count",
        title="Ventas por subcategoría",
    )
    st.plotly_chart(fig_subcat, use_container_width=True)
