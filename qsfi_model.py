import pandas as pd

def qsi(file):
    df = pd.read_csv(file)
    df["T1_us"] = df["T1"] * 1_000_000
    df["T2_us"] = df["T2"] * 1_000_000
    df["QSI"] = (df["T1_us"] + df["T2_us"]) / 2
    return df[["Qubit", "QSI"]]

d1 = qsi("quantum_data_day1.csv").rename(columns={"QSI": "Day1"})
d2 = qsi("quantum_data_day2.csv").rename(columns={"QSI": "Day2"})
d3 = qsi("quantum_data_day3.csv").rename(columns={"QSI": "Day3"})
d4 = qsi("quantum_data_day4.csv").rename(columns={"QSI": "Day4"})

df = d1.merge(d2, on="Qubit").merge(d3, on="Qubit").merge(d4, on="Qubit")

df["Average_QSI"] = df[["Day1", "Day2", "Day3", "Day4"]].mean(axis=1)
df["Trend"] = df["Day4"] - df["Day1"]

df["QSFI"] = df["Day4"] + (df["Trend"] * 0.5)

def risk(row):
    if row["QSFI"] >= 180 and row["Trend"] >= -20:
        return "Low Risk"
    elif row["QSFI"] < 80 or row["Trend"] < -50:
        return "High Risk"
    else:
        return "Medium Risk"

df["Future_Risk"] = df.apply(risk, axis=1)

print("\nFuture Risk Summary")
print(df["Future_Risk"].value_counts())

print("\nTop 10 Low Risk Qubits")
print(df[df["Future_Risk"] == "Low Risk"].sort_values("QSFI", ascending=False).head(10))

print("\nTop 10 High Risk Qubits")
print(df[df["Future_Risk"] == "High Risk"].sort_values("QSFI").head(10))