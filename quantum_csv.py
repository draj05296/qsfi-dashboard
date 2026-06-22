from qiskit_ibm_runtime import QiskitRuntimeService
import pandas as pd

service = QiskitRuntimeService()

backend = service.backends()[0]
properties = backend.properties()

data = []

for q in range(backend.num_qubits):
    try:
        t1 = properties.t1(q)
    except:
        t1 = None

    try:
        t2 = properties.t2(q)
    except:
        t2 = None

    data.append([q, t1, t2])

df = pd.DataFrame(data, columns=["Qubit", "T1", "T2"])

df.to_csv("quantum_data.csv", index=False)

print("CSV file created successfully!")