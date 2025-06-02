from pathlib import Path
from typing import IO

import polars as pl


def read_superstore_data(
    superstore_source: str | Path | IO[str] | IO[bytes] | bytes,
) -> pl.DataFrame:
    return pl.read_csv(
        source=superstore_source,
        schema={
            "Row ID": pl.UInt32,
            "Order ID": pl.String,
            "Order Date": pl.String,
            "Ship Date": pl.String,
            "Ship Mode": pl.Categorical,
            "Customer ID": pl.Categorical,
            "Customer Name": pl.Categorical,
            "Segment": pl.Categorical,
            "Country": pl.Categorical,
            "City": pl.Categorical,
            "State": pl.Categorical,
            "Postal Code": pl.Categorical,
            "Region": pl.Categorical,
            "Product ID": pl.Categorical,
            "Category": pl.Categorical,
            "Sub-Category": pl.Categorical,
            "Product Name": pl.Categorical,
            "Sales": pl.Float64,
            "Quantity": pl.UInt8,
            "Discount": pl.Float64,
            "Profit": pl.Float64,
        },
    ).with_columns(
        pl.col("Order Date").str.to_date("%m/%d/%Y"),
        pl.col("Ship Date").str.to_date("%m/%d/%Y"),
    )
