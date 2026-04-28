import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Load dataset
df = pd.read_csv("sales_data.csv")

# Convert date
df["Order Date"] = pd.to_datetime(df["Order Date"], dayfirst=True)

# Sort by date
df = df.sort_values("Order Date")

# Aggregate sales by month
df["Month"] = df["Order Date"].dt.to_period("M")
monthly_sales = df.groupby("Month")["Sales"].sum().reset_index()

# Convert month to numeric index
monthly_sales["Month_Index"] = range(len(monthly_sales))

# Features & target
X = monthly_sales[["Month_Index"]]
y = monthly_sales["Sales"]

# Model
model = LinearRegression()
model.fit(X, y)

# Predictions
monthly_sales["Predicted"] = model.predict(X)

# ---- Plot ----
plt.figure()
plt.plot(monthly_sales["Month_Index"], y, label="Actual Sales")
plt.plot(monthly_sales["Month_Index"], monthly_sales["Predicted"], linestyle='--', label="Predicted Sales")
plt.title("Sales Forecast (Linear Regression)")
plt.xlabel("Time (Months)")
plt.ylabel("Sales")
plt.legend()
plt.grid()

plt.savefig("sales_forecast.png")

print("Model complete.")