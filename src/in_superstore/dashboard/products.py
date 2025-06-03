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
    col1.metric("Unique products", n_products)
    col2.metric("Categories", n_categories)
    col3.metric("Subcategories", n_subcategories)

    st.subheader("Most sold products")

    top_products = (
        superstore_data.groupby("Product Name", observed=False)["Quantity"]
        .sum()
        .sort_values(ascending=False)
    )
    top_products = top_products.reset_index()
    st.dataframe(top_products, use_container_width=True, hide_index=True)

    st.subheader("Products with highest profit")

    margin_products = (
        superstore_data.groupby("Product Name", observed=False)["Profit"]
        .sum()
        .sort_values(ascending=False)
    )
    margin_products = margin_products.reset_index()
    st.dataframe(
        margin_products.style.format(
            {
                "Profit": "${:,.2f}",
            }
        ),
        use_container_width=True,
        hide_index=True,
    )

    st.subheader("Sales by category")
    category_sales = (
        superstore_data.groupby("Category", observed=False)["Order ID"]
        .nunique()
        .reset_index()
    )
    category_sales.columns = ["Category", "Count"]
    fig_cat = px.pie(
        category_sales, names="Category", values="Count", title="Sales by Category"
    )
    st.plotly_chart(fig_cat, use_container_width=True)
