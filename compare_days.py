import pandas as pd

day1 = pd.read_csv("quantum_data_day1.csv")
day2 = pd.read_csv("quantum_data_day2.csv")

day1["T1_us"] = day1["T1"] * 1_000_000
day1["T2_us"] = day1["T2"] * 1_000_000
day1["QSI_Day1"] = (day1["T1_us"] + day1["T2_us"]) / 2

day2["T1_us"] = day2["T1"] * 1_000_000
day2["T2_us"] = day2["T2"] * 1_000_000
day2["QSI_Day2"] = (day2["T1_us"] + day2["T2_us"]) / 2

merged = pd.merge(
    day1[["Qubit", "QSI_Day1"]],
    day2[["Qubit", "QSI_Day2"]],
    on="Qubit"
)

merged["QSI_Change"] = merged["QSI_Day2"] - merged["QSI_Day1"]

print("Biggest Improved Qubits")
print(merged.sort_values("QSI_Change", ascending=False).head(10))

print("\nBiggest Degraded Qubits")
print(merged.sort_values("QSI_Change").head(10))