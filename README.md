# 🛒 E-Commerce Sales Analytics Dashboard

## 📌 Project Overview

The E-Commerce Sales Analytics Dashboard is an end-to-end data analytics project built using Python, PostgreSQL, SQL, and Streamlit.

The project analyzes e-commerce sales data and provides business insights through interactive dashboards, customer segmentation, sales trends, and sales forecasting.

This project demonstrates skills in:

- Data Analysis
- Data Visualization
- SQL & PostgreSQL
- Business Intelligence
- Customer Segmentation
- Sales Forecasting
- Streamlit Dashboard Development

---

## 🎯 Objectives

- Analyze overall sales performance.
- Identify top-performing products and categories.
- Understand customer purchasing behavior.
- Segment customers using RFM Analysis.
- Forecast future sales trends.
- Create an interactive dashboard for business users.

---

## 🛠️ Tech Stack

### Programming Language
- Python

### Database
- PostgreSQL

### Data Analysis Libraries
- Pandas
- NumPy

### Data Visualization
- Matplotlib
- Seaborn
- Plotly

### Machine Learning & Forecasting
- Scikit-Learn
- Statsmodels

### Dashboard Framework
- Streamlit

---

## 📂 Project Structure

```text
ecommerce_sales_dashboard/
│
├── app.py
├── requirements.txt
├── README.md
│
├── data/
│   └── ecommerce_sales.csv
│
├── database/
│   ├── db_connection.py
│   └── load_data.py
│
├── analysis/
│   ├── sales_analysis.py
│   ├── customer_segmentation.py
│   └── forecasting.py
│
├── tests/
│   ├── test_db.py
│   ├── test_analysis.py
│   ├── test_segmentation.py
│   └── test_forecasting.py
│
└── outputs/
```

---

## 📊 Features

### 1. Sales Overview Dashboard

Provides:

- Total Sales
- Total Orders
- Total Customers
- Average Order Value

---

### 2. Sales Analysis

Analyze:

- Sales by Category
- Sales by Product
- Monthly Sales Trend
- Region-wise Sales
- Profit Analysis

---

### 3. Customer Segmentation (RFM Analysis)

Customers are segmented using:

- Recency
- Frequency
- Monetary Value

Segments include:

- Champions
- Loyal Customers
- Potential Loyalists
- At Risk Customers
- Lost Customers

---

### 4. Sales Forecasting

Forecast future sales using time-series analysis.

Techniques used:

- Monthly Sales Aggregation
- Trend Analysis
- Forecast Visualization

---

### 5. Interactive Visualizations

Visual charts include:

- Bar Charts
- Line Charts
- Pie Charts
- Histograms
- Heatmaps

---

## 🗄️ Database Setup

### Create Database

```sql
CREATE DATABASE ecommerce_sales_db;
```

### Connect to PostgreSQL

Update database credentials in:

```python
db_connection.py
```

Example:

```python
conn = psycopg2.connect(
    host="localhost",
    database="ecommerce_sales_db",
    user="postgres",
    password="your_password"
)
```

---

## 🚀 Installation

### Clone Repository

```bash
git clone https://github.com/harish-ragavendra-12/ecommerce-sales-analytics-dashboard.git
cd ecommerce_sales_dashboard
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux/Mac

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 📥 Load Dataset

Place the dataset inside:

```text
data/ecommerce_sales.csv
```

Run data loading script:

```bash
python load_data.py
```

---

## ▶️ Run Application

```bash
streamlit run app.py
```

Application will open in browser at:

```text
http://localhost:8501
```

---

## 🧪 Testing

Run the following test scripts:

### Database Test

```bash
python test_db.py
```

### Analysis Test

```bash
python test_analysis.py
```

### Customer Segmentation Test

```bash
python test_segmentation.py
```

### Forecasting Test

```bash
python test_forecasting.py
```

---

## 📈 Business Insights Generated

- Best-selling products
- High revenue categories
- Customer lifetime value indicators
- Seasonal sales trends
- Future sales predictions
- Customer retention opportunities

---

## 📚 Skills Demonstrated

- Python Programming
- SQL Queries
- PostgreSQL Database Management
- Data Cleaning
- Exploratory Data Analysis (EDA)
- Customer Segmentation
- Sales Forecasting
- Dashboard Development
- Data Visualization
- Business Analytics

---

## 🔮 Future Enhancements

- Product Recommendation System
- Customer Churn Prediction
- Inventory Forecasting
- Advanced Machine Learning Models
- Real-Time Dashboard Updates
- Cloud Deployment

---

## 👨‍💻 Author

Harish Ragavendra

Aspiring Data Analyst / Data Scientist

---

## ⭐ Project Outcome

This project showcases practical data analytics skills by transforming raw e-commerce sales data into meaningful business insights through dashboards, customer segmentation, and forecasting techniques.