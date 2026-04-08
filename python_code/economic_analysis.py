import pandas as pd
import matplotlib.pyplot as plt

# Load datasets
inflation = pd.read_csv("csv/inflation.csv", skiprows=4)
unemployment = pd.read_csv("csv/unemployment.csv", skiprows=4)

# Filter for South Africa
country = "South Africa"

inflation_sa = inflation[inflation["Country Name"] == country]
unemployment_sa = unemployment[unemployment["Country Name"] == country]

# Select years
years = [str(year) for year in range(2000, 2023)]

inflation_values = inflation_sa[years].values.flatten()
unemployment_values = unemployment_sa[years].values.flatten()

# Create DataFrame
df = pd.DataFrame({
    "Year": list(range(2000, 2023)),
    "Inflation": inflation_values,
    "Unemployment": unemployment_values
})

# Clean missing values
df = df.dropna()

# ---- PLOT 1: Inflation Trend ----
plt.figure()
plt.plot(df["Year"], df["Inflation"])
plt.title("Inflation Trend (South Africa)")
plt.xlabel("Year")
plt.ylabel("Inflation (%)")
plt.grid()
plt.savefig("inflation_trend.png")

# ---- PLOT 2: Unemployment Trend ----
plt.figure()
plt.plot(df["Year"], df["Unemployment"])
plt.title("Unemployment Trend (South Africa)")
plt.xlabel("Year")
plt.ylabel("Unemployment (%)")
plt.grid()
plt.savefig("unemployment_trend.png")

# ---- PLOT 3: Relationship ----
plt.figure()
plt.scatter(df["Inflation"], df["Unemployment"])
plt.title("Inflation vs Unemployment")
plt.xlabel("Inflation (%)")
plt.ylabel("Unemployment (%)")
plt.grid()
plt.savefig("relationship.png")

print("Analysis complete. Graphs saved.")
