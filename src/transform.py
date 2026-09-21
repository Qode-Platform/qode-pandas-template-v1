"""Pure frame-in / frame-out steps — each one independently testable."""

import pandas as pd


def drop_cancelled(df: pd.DataFrame) -> pd.DataFrame:
    return df.loc[df["amount"] > 0].copy()


def add_month(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    out["month"] = out["ordered_at"].dt.to_period("M").dt.to_timestamp()
    return out


def revenue_by_region(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.groupby(["region", "month"], observed=True, as_index=False)["amount"]
        .sum()
        .rename(columns={"amount": "revenue"})
        .sort_values(["region", "month"])
    )
