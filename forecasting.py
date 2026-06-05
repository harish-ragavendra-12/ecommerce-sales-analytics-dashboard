import pandas as pd
import numpy as np

from sklearn.linear_model import LinearRegression


def forecast_sales(df):

    monthly = (
        df.groupby(
            pd.Grouper(
                key="order_date",
                freq="ME"
            )
        )["sales"]
        .sum()
        .reset_index()
    )

    monthly["month_number"] = (
        np.arange(len(monthly))
    )

    X = monthly[["month_number"]]

    y = monthly["sales"]

    model = LinearRegression()

    model.fit(X, y)

    future = pd.DataFrame({

        "month_number":
        np.arange(
            len(monthly),
            len(monthly) + 6
        )

    })

    future["forecast_sales"] = (
        model.predict(future)
    )

    return future