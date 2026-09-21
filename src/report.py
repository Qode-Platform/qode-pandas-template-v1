"""Pipeline entrypoint: `python -m src.report data/orders.csv`."""

import sys

from src.load import read_orders, write_parquet
from src.transform import add_month, drop_cancelled, revenue_by_region


def main(path: str) -> None:
    orders = read_orders(path)
    summary = revenue_by_region(add_month(drop_cancelled(orders)))
    write_parquet(summary, "artifacts/revenue_by_region.parquet")
    print(summary.to_string(index=False))


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "data/orders.csv")
