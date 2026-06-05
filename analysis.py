import pandas as pd


def prepare_data(df):

    df["order_date"] = pd.to_datetime(df["order_date"])

    return df


def get_total_revenue(df):

    return df["sales"].sum()


def get_total_orders(df):

    return len(df)


def get_total_customers(df):

    return df["customer_name"].nunique()


def get_average_order_value(df):

    return round(df["sales"].mean(), 2)


def sales_by_category(df):

    return (
        df.groupby("category")["sales"]
        .sum()
        .reset_index()
        .sort_values("sales", ascending=False)
    )


def sales_by_region(df):

    return (
        df.groupby("region")["sales"]
        .sum()
        .reset_index()
        .sort_values("sales", ascending=False)
    )


def top_products(df):

    return (
        df.groupby("product")["sales"]
        .sum()
        .reset_index()
        .sort_values("sales", ascending=False)
        .head(10)
    )


def top_customers(df):

    return (
        df.groupby("customer_name")["sales"]
        .sum()
        .reset_index()
        .sort_values("sales", ascending=False)
        .head(10)
    )


def monthly_sales(df):

    return (
        df.groupby(
            pd.Grouper(
                key="order_date",
                freq="ME"
            )
        )["sales"]
        .sum()
        .reset_index()
    )