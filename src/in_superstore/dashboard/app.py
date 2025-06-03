from pathlib import Path

import pandas as pd
import streamlit as st

from in_superstore import data_access
from in_superstore.dashboard import customers, products, sales, welcome


@st.cache_data
def fetch_superstore_data() -> pd.DataFrame:
    superstore_datapath = st.session_state.get("superstore_datapath")

    return data_access.superstore.read(superstore_datapath)


@st.cache_data
def fetch_geographic_data() -> pd.DataFrame:
    geographic_datapath = st.session_state.get("geographic_datapath")

    return data_access.geographic.read(geographic_datapath)


def get_pages() -> list[st.Page]:
    return [
        st.Page(page=welcome, title="Home", icon="🏠", default=True),
        st.Page(page=sales, title="Sales", icon="📊"),
        st.Page(page=products, title="Products", icon="🛍️"),
        st.Page(page=customers, title="Customers", icon="🧑"),
    ]


def run_app() -> None:
    st.set_page_config(layout="wide")

    data_dirname = st.secrets["data"]["data_dirname"]
    superstore_filename = st.secrets["data"]["superstore_filename"]
    geographic_filename = st.secrets["data"]["geographic_filename"]

    datapath = Path(data_dirname)
    superstore_datapath = datapath / superstore_filename
    geographic_datapath = datapath / geographic_filename

    st.session_state.setdefault("datapath", datapath)
    st.session_state.setdefault("superstore_datapath", superstore_datapath)
    st.session_state.setdefault("geographic_datapath", geographic_datapath)
    st.session_state.setdefault("superstore_data", fetch_superstore_data())
    st.session_state.setdefault("geographic_data", fetch_geographic_data())

    st.navigation(get_pages()).run()


if __name__ == "__main__":
    run_app()
