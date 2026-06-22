import pandas as pd

df = pd.read_csv("quantum_data.csv")

print("Total Qubits:", len(df))

print("\nT1 Statistics")
print("Max T1:", df["T1"].max())
print("Min T1:", df["T1"].min())
print("Average T1:", df["T1"].mean())

print("\nT2 Statistics")
print("Max T2:", df["T2"].max())
print("Min T2:", df["T2"].min())
print("Average T2:", df["T2"].mean())