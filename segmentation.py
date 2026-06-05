import pandas as pd


def customer_segmentation(df):

    customer_sales = (
        df.groupby("customer_name")["sales"]
        .sum()
        .reset_index()
    )

    def assign_segment(total_sales):

        if total_sales >= 30000:
            return "High Value"

        elif total_sales >= 15000:
            return "Medium Value"

        else:
            return "Low Value"

    customer_sales["segment"] = (
        customer_sales["sales"]
        .apply(assign_segment)
    )

    return customer_sales