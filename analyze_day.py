import pandas as pd

df = pd.read_csv("quantum_data_day5.csv")

df["T1_us"] = df["T1"] * 1_000_000
df["T2_us"] = df["T2"] * 1_000_000

print("Total Qubits:", len(df))
print("Missing T2:", df["T2"].isna().sum())

print("\nT1 in microseconds")
print("Max:", df["T1_us"].max())
print("Min:", df["T1_us"].min())
print("Average:", df["T1_us"].mean())

print("\nT2 in microseconds")
print("Max:", df["T2_us"].max())
print("Min:", df["T2_us"].min())
print("Average:", df["T2_us"].mean())

df["QSI"] = (df["T1_us"] + df["T2_us"]) / 2

print("\nTop 10 Most Stable Qubits")
print(df.sort_values("QSI", ascending=False)[["Qubit", "T1_us", "T2_us", "QSI"]].head(10))

print("\nTop 10 Least Stable Qubits")
print(df.sort_values("QSI")[["Qubit", "T1_us", "T2_us", "QSI"]].head(10))