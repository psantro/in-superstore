import os
from pathlib import Path

import pandas as pd


def read() -> pd.DataFrame:
    """Read the US geography dataset.

    Raises:
        FileNotFoundError: If DATA_DIRNAME is not defined as an environment variable.
        FileNotFoundError: If GEO_FILENAME is not defined as an environment variable.

    Returns:
        pd.DataFrame: US geography dataset dataframe
    """

    data_dirname = os.getenv("DATA_DIRNAME", None)
    if data_dirname is None:
        msg = "Data directory not defined."
        raise FileNotFoundError(msg)

    geo_filename = os.getenv("GEO_FILENAME", None)
    if geo_filename is None:
        msg = "US geography dataset file not defined."
        raise FileNotFoundError(msg)

    geo_datapath = Path() / data_dirname / geo_filename

    geo_data = pd.read_csv(
        filepath_or_buffer=geo_datapath,
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
    )

    return geo_data[["postal_code", "latitude", "longitude"]]
