import streamlit as st
import pandas as pd
import plotly.express as px

from database import get_sales_data

from analysis import (
    prepare_data,
    get_total_revenue,
    get_total_orders,
    get_total_customers,
    get_average_order_value,
    sales_by_category,
    sales_by_region,
    top_products,
    top_customers,
    monthly_sales
)

from segmentation import customer_segmentation
from rfm import calculate_rfm
from forecasting import forecast_sales

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="E-Commerce Sales Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

# ---------------------------------------------------
# LOAD DATA
# ---------------------------------------------------

@st.cache_data
def load_data():
    df = get_sales_data()
    df = prepare_data(df)
    return df

df = load_data()

# ---------------------------------------------------
# HEADER
# ---------------------------------------------------

st.title("📊 E-Commerce Sales Analytics Dashboard")

st.markdown("---")

# ---------------------------------------------------
# SIDEBAR FILTERS
# ---------------------------------------------------

st.sidebar.header("Filters")

selected_regions = st.sidebar.multiselect(
    "Select Region",
    options=sorted(df["region"].unique()),
    default=sorted(df["region"].unique())
)

selected_categories = st.sidebar.multiselect(
    "Select Category",
    options=sorted(df["category"].unique()),
    default=sorted(df["category"].unique())
)

start_date = st.sidebar.date_input(
    "Start Date",
    value=df["order_date"].min()
)

end_date = st.sidebar.date_input(
    "End Date",
    value=df["order_date"].max()
)

# ---------------------------------------------------
# FILTER DATA
# ---------------------------------------------------

filtered_df = df[
    (df["region"].isin(selected_regions))
    &
    (df["category"].isin(selected_categories))
    &
    (df["order_date"] >= pd.to_datetime(start_date))
    &
    (df["order_date"] <= pd.to_datetime(end_date))
]

# ---------------------------------------------------
# KPI CARDS
# ---------------------------------------------------

st.subheader("Key Performance Indicators")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Revenue",
        f"₹{get_total_revenue(filtered_df):,.0f}"
    )

with col2:
    st.metric(
        "Total Orders",
        get_total_orders(filtered_df)
    )

with col3:
    st.metric(
        "Customers",
        get_total_customers(filtered_df)
    )

with col4:
    st.metric(
        "Avg Order Value",
        f"₹{get_average_order_value(filtered_df):,.0f}"
    )

st.markdown("---")

# ---------------------------------------------------
# SALES BY CATEGORY
# ---------------------------------------------------

category_df = sales_by_category(filtered_df)

fig_category = px.bar(
    category_df,
    x="category",
    y="sales",
    title="Sales by Category"
)

st.plotly_chart(
    fig_category,
    use_container_width=True
)

# ---------------------------------------------------
# SALES BY REGION
# ---------------------------------------------------

region_df = sales_by_region(filtered_df)

fig_region = px.pie(
    region_df,
    names="region",
    values="sales",
    title="Sales by Region"
)

st.plotly_chart(
    fig_region,
    use_container_width=True
)

# ---------------------------------------------------
# MONTHLY SALES TREND
# ---------------------------------------------------

monthly_df = monthly_sales(filtered_df)

fig_monthly = px.line(
    monthly_df,
    x="order_date",
    y="sales",
    markers=True,
    title="Monthly Sales Trend"
)

st.plotly_chart(
    fig_monthly,
    use_container_width=True
)

# ---------------------------------------------------
# TOP PRODUCTS & CUSTOMERS
# ---------------------------------------------------

col1, col2 = st.columns(2)

with col1:

    top_products_df = top_products(filtered_df)

    fig_products = px.bar(
        top_products_df,
        x="product",
        y="sales",
        title="Top Products"
    )

    st.plotly_chart(
        fig_products,
        use_container_width=True
    )

with col2:

    st.subheader("Top Customers")

    st.dataframe(
        top_customers(filtered_df),
        use_container_width=True
    )

st.markdown("---")

# ---------------------------------------------------
# DOWNLOAD REPORT
# ---------------------------------------------------

st.subheader("Download Report")

csv = filtered_df.to_csv(index=False)

st.download_button(
    label="📥 Download CSV Report",
    data=csv,
    file_name="sales_report.csv",
    mime="text/csv"
)

st.markdown("---")

# ---------------------------------------------------
# CUSTOMER SEGMENTATION
# ---------------------------------------------------

st.subheader("Customer Segmentation")

segments = customer_segmentation(filtered_df)

segment_summary = (
    segments["segment"]
    .value_counts()
    .reset_index()
)

segment_summary.columns = [
    "segment",
    "count"
]

fig_segment = px.bar(
    segment_summary,
    x="segment",
    y="count",
    title="Customer Segments"
)

st.plotly_chart(
    fig_segment,
    use_container_width=True
)

st.dataframe(
    segments,
    use_container_width=True
)

st.markdown("---")

# ---------------------------------------------------
# RFM ANALYSIS
# ---------------------------------------------------

st.subheader("RFM Analysis")

rfm_df = calculate_rfm(filtered_df)

st.dataframe(
    rfm_df,
    use_container_width=True
)

st.markdown("---")

# ---------------------------------------------------
# SALES FORECAST
# ---------------------------------------------------

st.subheader("6-Month Sales Forecast")

forecast_df = forecast_sales(filtered_df)

fig_forecast = px.line(
    forecast_df,
    x="month_number",
    y="forecast_sales",
    markers=True,
    title="Forecasted Sales"
)

st.plotly_chart(
    fig_forecast,
    use_container_width=True
)

st.markdown("---")

# ---------------------------------------------------
# BUSINESS INSIGHTS
# ---------------------------------------------------

st.subheader("Business Insights")

best_region = (
    region_df
    .sort_values("sales", ascending=False)
    .iloc[0]
)

best_category = (
    category_df
    .sort_values("sales", ascending=False)
    .iloc[0]
)

best_product = (
    top_products_df
    .sort_values("sales", ascending=False)
    .iloc[0]
)

st.success(
    f"🏆 Top Revenue Region: {best_region['region']}"
)

st.success(
    f"🏆 Best Selling Category: {best_category['category']}"
)

st.success(
    f"🏆 Best Selling Product: {best_product['product']}"
)

# ---------------------------------------------------
# RAW DATA
# ---------------------------------------------------

with st.expander("View Raw Data"):

    st.dataframe(
        filtered_df,
        use_container_width=True
    )