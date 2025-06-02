import streamlit as st
from dotenv import load_dotenv

from in_superstore import data_access

load_dotenv()

st.set_page_config(
    page_title="Dashboard Ejecutivo",
    page_icon=":clipboard:",
)

superstore_data = data_access.superstore.read()
geo_data = data_access.geo.read()

st.session_state.setdefault("superstore_data", superstore_data)
st.session_state.setdefault("geo_data", geo_data)

st.title("Dashboard Ejecutivo")
st.markdown(
    """
    ## Bienvenido al Dashboard Ejecutivo
    Este dashboard proporciona una visión general de los indicadores
    clave de rendimiento (KPI) de la empresa.

    ### Secciones del Dashboard:
    - **KPIs de Productos**: Visión general de los indicadores más importantes.
    - **KPIs de Ventas**: Detalles sobre las ventas por región y producto.

    Utiliza el menú lateral para navegar entre las diferentes secciones.
    """,
)

st.subheader("Datos Cargados")
st.dataframe(superstore_data)
st.dataframe(geo_data)
