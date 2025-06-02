import os
from pathlib import Path

import pandas as pd


def read() -> pd.DataFrame:
    """Read the superstore dataset.

    Raises:
        FileNotFoundError: If DATA_DIRNAME is not defined as an environment variable.
        FileNotFoundError: If SUPERSTORE_FILENAME is not defined as an environment variable.

    Returns:
        pd.DataFrame: Superstore dataset dataframe
    """

    data_dirname = os.getenv("DATA_DIRNAME", None)
    if data_dirname is None:
        msg = "Data directory not defined."
        raise FileNotFoundError(msg)

    superstore_filename = os.getenv("SUPERSTORE_FILENAME", None)
    if superstore_filename is None:
        msg = "Superstore dataset file not defined."
        raise FileNotFoundError(msg)

    superstore_datapath = Path() / data_dirname / superstore_filename

    superstore_data = pd.read_csv(
        filepath_or_buffer=superstore_datapath,
        index_col="Row ID",
        dtype={
            "Row ID": pd.UInt32Dtype(),
            "Order ID": pd.StringDtype(),
            "Order Date": pd.StringDtype(),
            "Ship Date": pd.StringDtype(),
            "Ship Mode": pd.CategoricalDtype(),
            "Customer ID": pd.CategoricalDtype(),
            "Customer Name": pd.CategoricalDtype(),
            "Segment": pd.CategoricalDtype(),
            "Country": pd.CategoricalDtype(),
            "City": pd.CategoricalDtype(),
            "State": pd.CategoricalDtype(),
            "Postal Code": pd.CategoricalDtype(),
            "Region": pd.CategoricalDtype(),
            "Product ID": pd.CategoricalDtype(),
            "Category": pd.CategoricalDtype(),
            "Sub-Category": pd.CategoricalDtype(),
            "Product Name": pd.CategoricalDtype(),
            "Sales": pd.Float64Dtype(),
            "Quantity": pd.UInt8Dtype(),
            "Discount": pd.Float64Dtype(),
            "Profit": pd.Float64Dtype(),
        },
    )

    superstore_data["Order Date"] = pd.to_datetime(superstore_data["Order Date"], format="%m/%d/%Y")
    superstore_data["Ship Date"] = pd.to_datetime(superstore_data["Ship Date"], format="%m/%d/%Y")

    return superstore_data
