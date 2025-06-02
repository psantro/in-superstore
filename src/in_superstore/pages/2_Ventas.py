import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Ventas",
    page_icon=":chart_with_upwards_trend:",
)

df = st.session_state.get("data", pd.DataFrame())
geo_df = st.session_state.get("geo_data", pd.DataFrame())

st.title("Ventas")

st.subheader("Mapa de ventas por ciudad")

pc_sales = df.groupby("Postal Code").size().reset_index(name="Ventas")

geo_sales = pd.merge(
    pc_sales,
    geo_df,
    left_on="Postal Code",
    right_on="postal_code",
    how="left",
)

geo_sales = geo_sales.dropna(subset=["latitude", "longitude"])

geo_sales = geo_sales.rename(columns={"latitude": "lat", "longitude": "lon"})

st.map(geo_sales[["lat", "lon", "Ventas"]], size="Ventas")

st.subheader("Gráfico de beneficios por año")

df["Order Date"] = pd.to_datetime(df["Order Date"])

yearly_profit = df.groupby(df["Order Date"].dt.year)["Profit"].sum().reset_index()
yearly_profit["Order Date"] = yearly_profit["Order Date"].astype(str)

st.line_chart(
    yearly_profit,
    x="Order Date",
    y="Profit",
    use_container_width=True,
)

st.subheader("Aumento del benedicio respecto al año anterior")

last_year_profit = yearly_profit.sort_values(by="Order Date", ascending=False).iloc[0]["Profit"]
compare_year_profit = yearly_profit.sort_values(by="Order Date", ascending=False).iloc[1]["Profit"]

st.metric(
    label="Incremento del beneficio del último año",
    value=f"${last_year_profit:,.2f}",
    delta=f"${last_year_profit - compare_year_profit:,.2f} ({((last_year_profit - compare_year_profit) / compare_year_profit) * 100:.2f}%)",
    delta_color="normal" if last_year_profit >= compare_year_profit else "inverse",
)
