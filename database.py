import pandas as pd
from sqlalchemy import create_engine

DATABASE_URL = (
    "postgresql+psycopg2://postgres:harish123@localhost:5432/ecommerce_dashboard"
)

engine = create_engine(DATABASE_URL)

def get_sales_data():

    query = """
    SELECT *
    FROM sales
    """

    df = pd.read_sql(query, engine)

    return df