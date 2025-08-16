import pandas as pd
import matplotlib.pyplot as plt

# Load CSV
df = pd.read_csv("sales_data.csv", parse_dates=["Date"])

# Total sales per region
region_sales = df.groupby("Region")["Sales"].sum()
region_sales.plot(kind="bar", title="Total Sales by Region")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("region_sales.png")
plt.clf()

# Sales by product
product_sales = df.groupby("Product")["Sales"].sum()
product_sales.plot(kind="pie", autopct="%1.1f%%", title="Product Sales Distribution")
plt.ylabel("")
plt.tight_layout()
plt.savefig("product_sales_pie.png")
plt.clf()

# Time-series trend
df.set_index("Date", inplace=True)
df.groupby("Date")["Sales"].sum().plot(title="Sales Over Time")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("sales_trend.png")
