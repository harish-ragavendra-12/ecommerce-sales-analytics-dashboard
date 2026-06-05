from database import get_sales_data
from analysis import *

df = get_sales_data()

df = prepare_data(df)

print("Total Revenue")
print(get_total_revenue(df))

print("\nTotal Orders")
print(get_total_orders(df))

print("\nTotal Customers")
print(get_total_customers(df))

print("\nAverage Order Value")
print(get_average_order_value(df))

print("\nSales By Category")
print(sales_by_category(df))

print("\nSales By Region")
print(sales_by_region(df))