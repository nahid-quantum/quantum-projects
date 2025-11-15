Bell State Entanglement (Qiskit Project)

This project demonstrates how to create a Bell State — one of the most fundamental entangled quantum states — using the Hadamard (H) and CNOT gates.

Entanglement is a uniquely quantum phenomenon where measuring one qubit immediately tells you the state of the other, no matter how far apart they are.

⸻

Quantum Circuit

q0 ──H────■──
      │
q1 ───────┼──
c0 <──────■──
c1 <──────────

from qiskit import QuantumCircuit, Aer, execute

# Create a 2-qubit circuit with 2 classical bits
qc = QuantumCircuit(2, 2)

# Apply Hadamard to put q0 in superposition
qc.h(0)

# Apply CNOT to create entanglement
qc.cx(0, 1)

# Measure both qubits
qc.measure([0, 1], [0, 1])

# Run the simulation
sim = Aer.get_backend('qasm_simulator')
result = execute(qc, sim, shots=1024).result()
counts = result.get_counts()

print("Measurement results:", counts)
qc.draw('mpl')

#Output

{'00': 508, '11': 516}

