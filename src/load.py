"""Ingest. Dtypes are declared here, never inferred in analysis code."""

from pathlib import Path

import pandas as pd

DTYPES = {
    "order_id": "int64",
    "customer": "string",
    "region": "category",
    "amount": "float64",
}


def read_orders(path: str | Path) -> pd.DataFrame:
    path = Path(path)
    if path.suffix == ".parquet":
        return pd.read_parquet(path)
    return pd.read_csv(path, dtype=DTYPES, parse_dates=["ordered_at"])


def write_parquet(df: pd.DataFrame, path: str | Path) -> None:
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(path, index=False)
