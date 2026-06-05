import pandas as pd


def calculate_rfm(df):

    snapshot_date = (
        df["order_date"].max()
        + pd.Timedelta(days=1)
    )

    rfm = df.groupby("customer_name").agg({

        "order_date":
        lambda x:
        (snapshot_date - x.max()).days,

        "order_id": "count",

        "sales": "sum"

    })

    rfm.columns = [
        "Recency",
        "Frequency",
        "Monetary"
    ]

    return rfm.reset_index()