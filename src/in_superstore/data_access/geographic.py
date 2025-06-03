from pathlib import Path

import pandas as pd


def read(geographic_datapath: Path) -> pd.DataFrame:
    return pd.read_csv(
        filepath_or_buffer=geographic_datapath,
        sep="\t",
        header=None,
        names=[
            "Country Code",
            "Postal Code",
            "Place Name",
            "Admin Name 1",
            "Admin Code 1",
            "Admin Name 2",
            "Admin Code 2",
            "Admin Name 3",
            "Admin Code 3",
            "Latitude",
            "Longitude",
            "Accuracy",
        ],
        index_col="Postal Code",
        usecols=[
            "Country Code",
            "Postal Code",
            "Place Name",
            "Latitude",
            "Longitude",
        ],
        dtype={
            "Country Code": pd.StringDtype(),
            "Postal Code": pd.StringDtype(),
            "Place Name": pd.StringDtype(),
            "Latitude": pd.Float64Dtype(),
            "Longitude": pd.Float64Dtype(),
        },
        skip_blank_lines=True,
        skipinitialspace=True,
    ).sort_index()
