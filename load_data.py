import pandas as pd
from sqlalchemy import create_engine

# Read CSV
df = pd.read_csv("data/ecommerce_sales.csv")

# Create sales column
df["sales"] = df["quantity"] * df["unit_price"]

# PostgreSQL Connection
engine = create_engine(
    "postgresql+psycopg2://postgres:harish123@localhost:5432/ecommerce_dashboard"
)

# Insert data
df.to_sql(
    "sales",
    engine,
    if_exists="replace",
    index=False
)

print("Data Loaded Successfully")