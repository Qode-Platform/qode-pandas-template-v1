import pandas as pd
import pytest

from src.transform import add_month, drop_cancelled, revenue_by_region


@pytest.fixture
def orders() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "region": pd.Series(["emea", "emea", "amer"], dtype="category"),
            "amount": [100.0, 0.0, 50.0],
            "ordered_at": pd.to_datetime(["2026-01-05", "2026-01-06", "2026-02-02"]),
        }
    )


def test_drop_cancelled_removes_zero_amounts(orders):
    assert len(drop_cancelled(orders)) == 2


def test_add_month_truncates_to_month_start(orders):
    assert add_month(orders)["month"].iloc[0] == pd.Timestamp("2026-01-01")


def test_revenue_by_region(orders):
    out = revenue_by_region(add_month(drop_cancelled(orders)))
    assert out.loc[out["region"] == "emea", "revenue"].iloc[0] == 100.0
