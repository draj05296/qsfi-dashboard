import pandas as pd

def qsi(file, day_name):
    df = pd.read_csv(file)

    df["T1_us"] = df["T1"] * 1_000_000
    df["T2_us"] = df["T2"] * 1_000_000

    df[day_name] = (df["T1_us"] + df["T2_us"]) / 2

    return df[["Qubit", day_name]]

d1 = qsi("quantum_data_day1.csv", "Day1")
d2 = qsi("quantum_data_day2.csv", "Day2")
d3 = qsi("quantum_data_day3.csv", "Day3")
d4 = qsi("quantum_data_day4.csv", "Day4")
d5 = qsi("quantum_data_day5.csv", "Day5")

df = d1.merge(d2,on="Qubit")
df = df.merge(d3,on="Qubit")
df = df.merge(d4,on="Qubit")
df = df.merge(d5,on="Qubit")

df["Average_QSI"] = df[
    ["Day1","Day2","Day3","Day4","Day5"]
].mean(axis=1)

df["Trend"] = df["Day5"] - df["Day1"]

df["QSFI"] = (
    df["Average_QSI"] * 0.7
    +
    df["Day5"] * 0.3
)

def risk(row):

    if row["QSFI"] > 180 and row["Trend"] > -20:
        return "Low Risk"

    elif row["QSFI"] < 80:
        return "High Risk"

    return "Medium Risk"

df["Risk"] = df.apply(risk, axis=1)

print("\nRisk Summary")
print(df["Risk"].value_counts())

print("\nTop 10 Low Risk Qubits")
print(
    df[df["Risk"]=="Low Risk"]
    .sort_values("QSFI", ascending=False)
    .head(10)
)

print("\nTop 10 High Risk Qubits")
print(
    df[df["Risk"]=="High Risk"]
    .sort_values("QSFI")
    .head(10)
)