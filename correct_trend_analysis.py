import pandas as pd

def prepare(file_name, day_name):
    df = pd.read_csv(file_name)
    df["T1_us"] = df["T1"] * 1_000_000
    df["T2_us"] = df["T2"] * 1_000_000
    df[f"{day_name}_QSI"] = (df["T1_us"] + df["T2_us"]) / 2
    return df[["Qubit", f"{day_name}_QSI"]]

day1 = prepare("quantum_data_day1.csv", "Day1")
day2 = prepare("quantum_data_day2.csv", "Day2")
day3 = prepare("quantum_data_day3.csv", "Day3")

trend = day1.merge(day2, on="Qubit").merge(day3, on="Qubit")

trend["Change_Day1_to_Day3"] = trend["Day3_QSI"] - trend["Day1_QSI"]

def classify(change):
    if change > 10:
        return "Improving"
    elif change < -10:
        return "Degrading"
    else:
        return "Stable"

trend["Trend"] = trend["Change_Day1_to_Day3"].apply(classify)

print("Top 10 Improving Qubits")
print(trend.sort_values("Change_Day1_to_Day3", ascending=False).head(10))

print("\nTop 10 Degrading Qubits")
print(trend.sort_values("Change_Day1_to_Day3").head(10))

print("\nTrend Summary")
print(trend["Trend"].value_counts())