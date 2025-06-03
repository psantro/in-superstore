import pandas as pd
import streamlit as st


def welcome() -> None:
    st.title("🛍️ Executive Dashboard 🛒")

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

    superstore_data = st.session_state.get("superstore_data", pd.DataFrame())
    geo_data = st.session_state.get("geographic_data", pd.DataFrame())
    
    st.dataframe(superstore_data)
    st.dataframe(geo_data)
