from qiskit_ibm_runtime import QiskitRuntimeService

service = QiskitRuntimeService()

backend = service.backends()[0]
properties = backend.properties()

print("Backend:", backend)
print("Qubits:", backend.num_qubits)

print("\nQubit 0 test values:")

try:
    print("T1:", properties.t1(0))
except Exception as e:
    print("T1 Error:", e)

try:
    print("T2:", properties.t2(0))
except Exception as e:
    print("T2 Error:", e)

try:
    print("Readout Error:", properties.readout_error(0))
except Exception as e:
    print("Readout Error:", e)

try:
    print("Gate Error X:", properties.gate_error("x", [0]))
except Exception as e:
    print("Gate Error X:", e)

try:
    print("Gate Error SX:", properties.gate_error("sx", [0]))
except Exception as e:
    print("Gate Error SX:", e)

try:
    print("Gate Error ID:", properties.gate_error("id", [0]))
except Exception as e:
    print("Gate Error ID:", e)