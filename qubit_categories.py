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

df = d1.merge(d2, on="Qubit")
df = df.merge(d3, on="Qubit")
df = df.merge(d4, on="Qubit")
df = df.merge(d5, on="Qubit")

df["Average"] = df[["Day1", "Day2", "Day3", "Day4", "Day5"]].mean(axis=1)

def category(row):
    values = [row["Day1"], row["Day2"], row["Day3"], row["Day4"], row["Day5"]]

    if row["Average"] > 180:
        return "Consistently Strong"

    if row["Average"] < 80:
        return "Consistently Weak"

    if values[-1] > values[0] + 30:
        return "Improving"

    return "Oscillating"

df["Category"] = df.apply(category, axis=1)

print("\nCategory Summary")
print(df["Category"].value_counts())

print("\nTop Strong Qubits")
print(df[df["Category"] == "Consistently Strong"].head(10))

print("\nTop Weak Qubits")
print(df[df["Category"] == "Consistently Weak"].head(10))