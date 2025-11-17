from qiskit import QuantumCircuit, Aer, execute
from math import pi

# Quantum teleportation circuit with 3 qubits and 3 classical bits
qc = QuantumCircuit(3, 3)

print("\nPreparing quantum teleportation protocol...\n")

# --- STEP 1: Prepare unknown state on Q0 ---
qc.ry(pi/3, 0)
qc.rz(pi/5, 0)

# --- STEP 2: Create entanglement between Q1 and Q2 ---
qc.h(1)
qc.cx(1, 2)

# --- STEP 3: Badr measurement by Ameena ---
qc.cx(0, 1)
qc.h(0)

# Measure Ameena's qubits
qc.measure(0, 0)
qc.measure(1, 1)

# --- STEP 4: Badr applies corrections based on Alice's classical bits ---
qc.cx(1, 2)
qc.cz(0, 2)

# Final measurement: Badr's qubit
qc.measure(2, 2)

# Run simulation
simulator = Aer.get_backend('qasm_simulator')
job = execute(qc, simulator, shots=1024)
result = job.result()
counts = result.get_counts()

print("=== Quantum Teleportation Results ===")
print(counts)
print("\nTeleportation complete.")