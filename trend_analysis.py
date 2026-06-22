import pandas as pd

# Load all 3 days
day1 = pd.read_csv("quantum_data_day1.csv")
day2 = pd.read_csv("quantum_data_day2.csv")
day3 = pd.read_csv("quantum_data_day3.csv")

# Create QSI
for df in [day1, day2, day3]:
    df["T1_us"] = df["T1"] * 1_000_000
    df["T2_us"] = df["T2"] * 1_000_000
    df["QSI"] = (df["T1_us"] + df["T2_us"]) / 2

# Merge
trend = pd.DataFrame({
    "Qubit": day1["Qubit"],
    "Day1_QSI": day1["QSI"],
    "Day2_QSI": day2["QSI"],
    "Day3_QSI": day3["QSI"]
})

# Calculate overall change
trend["Change"] = trend["Day3_QSI"] - trend["Day1_QSI"]

# Trend classification
def classify(change):
    if change > 10:
        return "Improving"
    elif change < -10:
        return "Degrading"
    else:
        return "Stable"

trend["Trend"] = trend["Change"].apply(classify)

print("\nTop 10 Improving Qubits")
print(trend.sort_values("Change", ascending=False).head(10))

print("\nTop 10 Degrading Qubits")
print(trend.sort_values("Change").head(10))

print("\nTrend Summary")
print(trend["Trend"].value_counts())