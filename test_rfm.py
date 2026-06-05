from database import get_sales_data
from analysis import prepare_data
from rfm import calculate_rfm

df = get_sales_data()

df = prepare_data(df)

rfm_df = calculate_rfm(df)

print(rfm_df.head())