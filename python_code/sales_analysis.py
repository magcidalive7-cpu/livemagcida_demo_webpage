import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("sales_data.csv")

# Clean column names
df.columns = df.columns.str.strip()

# Convert dates (South African / DD/MM/YYYY format)
df["Order Date"] = pd.to_datetime(df["Order Date"], dayfirst=True)

# Extract year
df["Year"] = df["Order Date"].dt.year

# --------------------------------------------------
# CREATE ESTIMATED PROFIT COLUMN (since dataset has no Profit)
# Real analysts sometimes estimate profit using margin assumptions
# --------------------------------------------------

profit_margin = {
    "Furniture": 0.08,         # 8%
    "Office Supplies": 0.15,   # 15%
    "Technology": 0.20         # 20%
}

# Apply category margin
df["Profit"] = df.apply(
    lambda row: row["Sales"] * profit_margin.get(row["Category"], 0.10),
    axis=1
)

# ---- 1. SALES TREND ----
sales_trend = df.groupby("Year")["Sales"].sum()

plt.figure()
sales_trend.plot(marker="o")
plt.title("Total Sales Over Time")
plt.xlabel("Year")
plt.ylabel("Sales")
plt.grid()
plt.tight_layout()
plt.savefig("sales_trend.png")

# ---- 2. PROFIT BY CATEGORY ----
profit_category = df.groupby("Category")["Profit"].sum()

plt.figure()
profit_category.plot(kind="bar")
plt.title("Estimated Profit by Category")
plt.xlabel("Category")
plt.ylabel("Profit")
plt.grid()
plt.tight_layout()
plt.savefig("profit_category.png")

# ---- 3. SALES BY REGION ----
region_sales = df.groupby("Region")["Sales"].sum()

plt.figure()
region_sales.plot(kind="bar")
plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.grid()
plt.tight_layout()
plt.savefig("region_sales.png")

# ---- 4. SALES VS PROFIT ----
plt.figure()
plt.scatter(df["Sales"], df["Profit"])
plt.title("Sales vs Estimated Profit")
plt.xlabel("Sales")
plt.ylabel("Profit")
plt.grid()
plt.tight_layout()
plt.savefig("sales_vs_profit.png")

# ---- 5. TOP 10 PRODUCTS BY SALES ----
top_products = df.groupby("Product Name")["Sales"].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(12,6))
top_products.plot(kind="bar")
plt.title("Top 10 Products by Sales")
plt.xlabel("Product Name")
plt.ylabel("Sales")
plt.grid()
plt.tight_layout()
plt.savefig("top_products.png")

print("Sales + Estimated Profit analysis complete.")
print(df[["Category", "Sales", "Profit"]].head())
