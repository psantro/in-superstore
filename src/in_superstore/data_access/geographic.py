from pathlib import Path

import pandas as pd


def read(geographic_datapath: Path) -> pd.DataFrame:
    return pd.read_csv(
        filepath_or_buffer=geographic_datapath,
        sep="\t",
        header=None,
        names=[
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
        ],
        usecols=[
            "country_code",
            "postal_code",
            "place_name",
            "latitude",
            "longitude",
        ],
        dtype={
            "country_code": pd.StringDtype(),
            "postal_code": pd.StringDtype(),
            "place_name": pd.StringDtype(),
            "latitude": pd.Float64Dtype(),
            "longitude": pd.Float64Dtype(),
        },
        skipinitialspace=True,
    )
