import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Productos",
    page_icon=":package:",
)

superstore_data = st.session_state.get("superstore_data", pd.DataFrame())

n_products = superstore_data["Product Name"].nunique()

st.title("Productos")

st.subheader("Productos más vendidos")

show_top_products = st.number_input(
    "Número de productos a mostrar",
    min_value=1,
    max_value=n_products,
    value=5,
    step=1,
    key="top_products_input",
)

top_products = (
    superstore_data.groupby("Product Name")["Quantity"]
    .sum()
    .sort_values(ascending=False)
    .head(show_top_products)
)
top_products = top_products.reset_index()
top_products.columns = ["Nombre del producto", "Ventas"]
st.table(top_products)

st.subheader("Productos con mayor margen de beneficio")

show_margin_products = st.number_input(
    "Número de productos a mostrar",
    min_value=1,
    max_value=n_products,
    value=5,
    step=1,
    key="margin_products_input",
)

margin_products = (
    superstore_data.groupby("Product Name")["Profit"]
    .sum()
    .sort_values(ascending=False)
    .head(show_margin_products)
)
margin_products = margin_products.reset_index()
margin_products.columns = ["Nombre del producto", "Margen de beneficio"]
st.table(margin_products)
