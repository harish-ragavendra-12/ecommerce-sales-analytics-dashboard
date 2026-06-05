import pandas as pd
import random
from faker import Faker

fake = Faker()

regions = ["North", "South", "East", "West"]

categories = {
    "Electronics": ["Laptop", "Mobile", "Headphones"],
    "Fashion": ["T-Shirt", "Jeans", "Shoes"],
    "Home": ["Chair", "Table", "Lamp"]
}

rows = []

for i in range(1, 501):

    category = random.choice(list(categories.keys()))
    product = random.choice(categories[category])

    quantity = random.randint(1, 5)
    unit_price = random.randint(500, 5000)

    rows.append([
        f"ORD{i:04}",
        fake.date_between(start_date="-1y", end_date="today"),
        fake.name(),
        random.choice(regions),
        category,
        product,
        quantity,
        unit_price
    ])

df = pd.DataFrame(
    rows,
    columns=[
        "order_id",
        "order_date",
        "customer_name",
        "region",
        "category",
        "product",
        "quantity",
        "unit_price"
    ]
)

df.to_csv("ecommerce_sales.csv", index=False)

print("Dataset Generated Successfully")