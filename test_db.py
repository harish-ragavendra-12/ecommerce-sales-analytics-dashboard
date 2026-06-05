from database import get_sales_data

df = get_sales_data()

print(df.head())

print("\nRows and Columns")

print(df.shape)