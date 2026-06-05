from database import get_sales_data
from analysis import prepare_data
from segmentation import customer_segmentation

df = get_sales_data()

df = prepare_data(df)

segments = customer_segmentation(df)

print(segments.head())

print("\nSegment Counts")

print(
    segments["segment"]
    .value_counts()
)