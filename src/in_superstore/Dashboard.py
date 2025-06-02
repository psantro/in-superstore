import pandas as pd
import streamlit as st

from in_superstore.read import read_superstore_data

st.set_page_config(
    page_title="Dashboard Ejecutivo",
    page_icon=":clipboard:",
)

df = read_superstore_data("../../data/Sample - Superstore.csv")

geo_cols = [
    "country_code",
    "postal_code",
    "place_name",
    "admin_name1",
    "admin_code1",
    "admin_name2",
    "admin_code2",
    "admin_name3",
    "admin_code3",
    "latitude",
    "longitude",
    "accuracy",
]

geo_df = pd.read_csv("../../data/US.txt", sep="\t", header=None, names=geo_cols)
geo_df = geo_df[["postal_code", "latitude", "longitude"]]

st.session_state.setdefault("data", df)
st.session_state.setdefault("geo_data", geo_df)

st.title("Dashboard Ejecutivo")
st.markdown(
    """
    ## Bienvenido al Dashboard Ejecutivo
    Este dashboard proporciona una visión general de los indicadores clave de rendimiento (KPI) de la empresa.

    ### Secciones del Dashboard:
    - **KPIs de Productos**: Visión general de los indicadores más importantes.
    - **KPIs de Ventas**: Detalles sobre las ventas por región y producto.

    Utiliza el menú lateral para navegar entre las diferentes secciones.
    """,
)

st.subheader("Datos Cargados")
st.dataframe(df)
st.dataframe(geo_df)
