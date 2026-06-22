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

    try:
        readout_error = properties.readout_error(q)
    except:
        readout_error = None

    try:
        gate_error = properties.gate_error("sx", [q])
    except:
        gate_error = None

    data.append([q, t1, t2, readout_error, gate_error])

df = pd.DataFrame(
    data,
    columns=["Qubit", "T1", "T2", "Readout_Error", "Gate_Error"]
)

df.to_csv("quantum_full_data.csv", index=False)

print("Full quantum dataset created successfully!")