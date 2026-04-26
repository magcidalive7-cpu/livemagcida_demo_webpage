import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("sales_data.csv")

# Convert date
df["Order Date"] = pd.to_datetime(df["Order Date"])

# Extract year
df["Year"] = df["Order Date"].dt.year

# ---- 1. SALES TREND ----
sales_trend = df.groupby("Year")["Sales"].sum()

plt.figure()
sales_trend.plot()
plt.title("Total Sales Over Time")
plt.xlabel("Year")
plt.ylabel("Sales")
plt.grid()
plt.savefig("sales_trend.png")

# ---- 2. PROFIT BY CATEGORY ----
profit_category = df.groupby("Category")["Profit"].sum()

plt.figure()
profit_category.plot(kind='bar')
plt.title("Profit by Category")
plt.xlabel("Category")
plt.ylabel("Profit")
plt.grid()
plt.savefig("profit_category.png")

# ---- 3. SALES BY REGION ----
region_sales = df.groupby("Region")["Sales"].sum()

plt.figure()
region_sales.plot(kind='bar')
plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.grid()
plt.savefig("region_sales.png")

# ---- 4. SALES VS PROFIT ----
plt.figure()
plt.scatter(df["Sales"], df["Profit"])
plt.title("Sales vs Profit")
plt.xlabel("Sales")
plt.ylabel("Profit")
plt.grid()
plt.savefig("sales_vs_profit.png")

print("Sales analysis complete.")
