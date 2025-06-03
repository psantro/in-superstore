import os
from pathlib import Path

import pandas as pd
import streamlit as st
from dotenv import load_dotenv

from in_superstore import data_access
from in_superstore.dashboard import other, welcome

load_dotenv()


@st.cache_data
def fetch_superstore_data() -> pd.DataFrame:
    data_dirname = os.getenv("DATA_DIRNAME", None)
    if data_dirname is None:
        msg = "Data directory not defined."
        raise FileNotFoundError(msg)

    superstore_filename = os.getenv("SUPERSTORE_FILENAME", None)
    if superstore_filename is None:
        msg = "Superstore dataset file not defined."
        raise FileNotFoundError(msg)

    superstore_datapath = Path() / data_dirname / superstore_filename

    return data_access.superstore.read(superstore_datapath)


@st.cache_data
def fetch_geographic_data() -> pd.DataFrame:
    data_dirname = os.getenv("DATA_DIRNAME", None)
    if data_dirname is None:
        msg = "Data directory not defined."
        raise FileNotFoundError(msg)

    geographic_filename = os.getenv("GEO_FILENAME", None)
    if geographic_filename is None:
        msg = "US geography dataset file not defined."
        raise FileNotFoundError(msg)

    geographic_datapath = Path() / data_dirname / geographic_filename

    return data_access.geographic.read(geographic_datapath)


def get_pages() -> list[st.Page]:
    return [
        st.Page(page=welcome, title="Welcome!", icon="🏠"),
        st.Page(page=other, title="Other!", icon="💬"),
    ]


def run_app() -> None:
    st.session_state.setdefault("superstore_data", fetch_superstore_data())
    st.session_state.setdefault("geographic_data", fetch_geographic_data())

    st.navigation(get_pages()).run()


if __name__ == "__main__":
    run_app()
