import pandas as pd

df = pd.read_csv("quantum_full_data.csv")

df["T1_us"] = df["T1"] * 1_000_000
df["T2_us"] = df["T2"] * 1_000_000

df["Base_QSI"] = (df["T1_us"] + df["T2_us"]) / 2

df["Readout_Error_Percent"] = df["Readout_Error"] * 100
df["Gate_Error_Percent"] = df["Gate_Error"] * 100

df["Enhanced_QSI"] = (
    df["Base_QSI"]
    - (df["Readout_Error_Percent"] * 5)
    - (df["Gate_Error_Percent"] * 10)
)

print("Top 10 Best Qubits by Enhanced QSI")
print(df.sort_values("Enhanced_QSI", ascending=False)[
    ["Qubit", "T1_us", "T2_us", "Readout_Error_Percent", "Gate_Error_Percent", "Enhanced_QSI"]
].head(10))

print("\nTop 10 Worst Qubits by Enhanced QSI")
print(df.sort_values("Enhanced_QSI")[
    ["Qubit", "T1_us", "T2_us", "Readout_Error_Percent", "Gate_Error_Percent", "Enhanced_QSI"]
].head(10))