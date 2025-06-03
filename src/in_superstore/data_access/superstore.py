from pathlib import Path

import pandas as pd


def read(superstore_datapath: Path) -> pd.DataFrame:
    superstore_data = pd.read_csv(
        filepath_or_buffer=superstore_datapath,
        index_col="Order ID",
        dtype={
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
        skip_blank_lines=True,
        skipinitialspace=True,
    )

    superstore_data = superstore_data.drop(labels=["Row ID"], axis="columns")

    superstore_data["Order Date"] = pd.to_datetime(
        superstore_data["Order Date"], format="%m/%d/%Y"
    )
    superstore_data["Ship Date"] = pd.to_datetime(
        superstore_data["Ship Date"], format="%m/%d/%Y"
    )

    return superstore_data.sort_values(by="Order Date", ascending=False)
