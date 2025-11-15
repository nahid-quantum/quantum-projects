## Single-Qubit Superposition (Qiskit Project)

This project demonstrates how a single qubit can enter a state of superposition using the Hadamard (H) gate.  
Superposition allows a qubit to exist in both |0⟩ and |1⟩ at the same time until measured.

### Quantum Circuit

q0 ──H───■───  
        │  
c0 <────■────  

### Code (Qiskit)

from qiskit import QuantumCircuit, Aer, execute

# Create a 1-qubit circuit with 1 classical bit
qc = QuantumCircuit(1, 1)

# Apply Hadamard gate to create superposition
qc.h(0)

# Measure the qubit
qc.measure(0, 0)

# Run the simulation
sim = Aer.get_backend('qasm_simulator')
result = execute(qc, sim, shots=1024).result()
counts = result.get_counts()

print("Measurement results:", counts)
qc.draw('mpl')

### Expected Output

Approximately 50% |0⟩ and 50% |1⟩  
Example:  
{'0': 520, '1': 504}

### What You Learn

- How qubits differ from classical bits  
- How the Hadamard gate works  
- How measurement collapses a quantum state  
- How to simulate quantum circuits using Qiskit
