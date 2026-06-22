import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="QSFI Dashboard",
    layout="wide"
)

st.title("🚀 Quantum Stability Forecast Index (QSFI)")
st.subheader("IBM Fez Quantum Processor Analysis")

st.markdown("---")

st.header("Project Overview")

st.write("""
This dashboard analyzes IBM Quantum calibration data collected over 5 days.

Features:
- Day-wise calibration data
- Qubit Stability Analysis
- QSI Rankings
- QSFI Forecast Results
- Risk Classification
""")

st.markdown("---")

st.header("Risk Distribution")

risk_data = {
    "Risk": ["Low Risk", "Medium Risk", "High Risk"],
    "Count": [6, 134, 16]
}

risk_df = pd.DataFrame(risk_data)

col1, col2, col3 = st.columns([1,2,1])

with col2:
    fig, ax = plt.subplots(figsize=(4,4))

    ax.pie(
        risk_df["Count"],
        labels=risk_df["Risk"],
        autopct="%1.1f%%"
    )

    st.pyplot(fig)

st.markdown("---")

st.header("Qubit Recommendations")

files = [
    "quantum_data_day1.csv",
    "quantum_data_day2.csv",
    "quantum_data_day3.csv",
    "quantum_data_day4.csv",
    "quantum_data_day5.csv"
]

selected_file = st.selectbox(
    "Select Dataset",
    files
)

df = pd.read_csv(selected_file)
# QSFI Calculation
df["QSFI_Score"] = ((df["T1"] + df["T2"]) / 2) * 1000000
# Risk Classification

def classify_risk(score):
    if score >= 150:
        return "Low Risk"
    elif score >= 100:
        return "Medium Risk"
    else:
        return "High Risk"

df["Risk"] = df["QSFI_Score"].apply(classify_risk)
df["QSFI_Score"] = (
    (df["T1"] / df["T1"].max()) * 50 +
    (df["T2"] / df["T2"].max()) * 50
)
st.write("Columns:")
st.write(df.columns.tolist())

st.write("First 5 Rows:")
st.dataframe(df.head())
st.subheader("QSFI Score Preview")
st.dataframe(
    df[["Qubit", "QSFI_Score", "Risk"]].head(10)
)

st.subheader(f"Preview: {selected_file}")

st.dataframe(df)

st.success(f"Loaded {len(df)} qubits")
st.markdown("---")
st.markdown("---")

st.header("Top 10 Best Forecasted Qubits")

top10 = df.sort_values(
    by="QSFI_Score",
    ascending=False
).head(10)

st.dataframe(
    top10[["Qubit", "T1", "T2", "QSFI_Score"]]
)
st.header("Project Statistics")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Days Collected", "5")
col2.metric("Total Qubits", "156")
col3.metric("Low Risk", "6")
col4.metric("High Risk", "16")

st.markdown("---")

st.header("IBM Fez Stability Trend")

st.image(
    "stability_trend.png",
    caption="Average T1 and T2 across collected days"
)

st.markdown("---")

st.header("QSFI Version 2 Results")

st.write("""
Low Risk Qubits: 6

Medium Risk Qubits: 134

High Risk Qubits: 16

Best Forecasted Qubit:
Qubit 15

Worst Forecasted Qubit:
Qubit 149
""")

st.markdown("---")
st.header("Top 10 Best Forecasted Qubits")
st.markdown("---")
st.subheader("QSFI Formula")

st.latex(r"QSFI = \frac{T1 + T2}{2}")

st.write("""
QSFI (Quantum Stability Forecast Index) is a research metric
developed to evaluate qubit stability using coherence times.

Higher QSFI values indicate more stable qubits.
""")

best_qubits = pd.DataFrame({
    "Rank": [1,2,3,4,5,6,7,8,9,10],
    "Qubit": [15,13,3,2,83,132,120,110,45,76],
    "QSFI Score": [98.5,97.8,97.1,96.9,96.4,95.8,95.2,94.9,94.5,94.1]
})
    


st.dataframe(best_qubits)

st.markdown("---")
st.header("Qubit Recommendations")

col1, col2 = st.columns(2)

with col1:
    st.success("""
### Recommended (Low Risk)

Qubit 15

Qubit 13

Qubit 3

Qubit 2

Qubit 83

Qubit 132
""")

with col2:
    st.error("""
### Avoid (High Risk)

Qubit 149

Qubit 0

Qubit 66

Qubit 98

Qubit 107

Qubit 51
""")