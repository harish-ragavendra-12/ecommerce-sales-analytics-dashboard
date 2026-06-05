from database import get_sales_data
from analysis import prepare_data
from forecasting import forecast_sales

df = get_sales_data()

df = prepare_data(df)

forecast = forecast_sales(df)

print(forecast)