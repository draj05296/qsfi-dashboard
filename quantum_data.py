from qiskit_ibm_runtime import QiskitRuntimeService

service = QiskitRuntimeService()

backend = service.backends()[0]

properties = backend.properties()

print("Backend:", backend)
print("Qubits:", backend.num_qubits)

for q in range(10):
    print(
        "Qubit", q,
        "T1 =", properties.t1(q),
        "T2 =", properties.t2(q)
    )