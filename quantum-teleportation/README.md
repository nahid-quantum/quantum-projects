# Quantum Teleportation Protocol

This project demonstrates **Quantum Teleportation**, a fundamental quantum information protocol that transfers an unknown qubit state from one place (Ameena) to another (Badr) *without physically sending the qubit itself*.

The process depends on:
- Quantum entanglement  
- Bell-state measurement  
- Classical communication  
- Conditional quantum gates for state reconstruction  

---

##  Goal
Teleport the unknown state:

|ψ> = α|0⟩ + β|1⟩

from **Ameena** to **Badr** using:
- 3 qubits  
- 2 classical bits  
- Entanglement + measurement + classical messages  

---

##  Circuit Overview

Q0 → the unknown state (Ameena)  
Q1 → Ameena's half of the entangled pair  
Q2 → Badr's half of the entangled pair  

Steps:
1. Ameena prepares |ψ>  
2. Create entanglement between Q1 and Q2  
3. Ameena performs Bell-state measurement  
4. Send measurement results to Bob (classical)  
5. Badr applies X / Z gates to reconstruct |ψ> exactly  

---

##  Python Code Implementation (Qiskit)

```python
from qiskit import QuantumCircuit, Aer, execute
from math import pi

# Quantum teleportation circuit with 3 qubits and 3 classical bits
qc = QuantumCircuit(3, 3)

# --- STEP 1: Prepare unknown state on Q0 ---
qc.ry(pi/3, 0)
qc.rz(pi/5, 0)

# --- STEP 2: Create entanglement between Q1 and Q2 ---
qc.h(1)
qc.cx(1, 2)

# --- STEP 3: Bell measurement by Alice ---
qc.cx(0, 1)
qc.h(0)

# Measure Alice’s qubits
qc.measure(0, 0)
qc.measure(1, 1)

# --- STEP 4: Bob applies corrections based on Alice's classical bits ---
qc.cx(1, 2)
qc.cz(0, 2)

# Final measurement: Bob’s qubit
qc.measure(2, 2)

# Run simulation
simulator = Aer.get_backend('qasm_simulator')
job = execute(qc, simulator, shots=1024)
result = job.result()
counts = result.get_counts()

print("\n=== Quantum Teleportation Results ===")
print(counts)
```

---

## Output


```
{'001': 260, '111': 252, '101': 256, '011': 256}
```

Your exact values may differ because of randomness.

---


##  Requirements

Install Qiskit:

```
pip install qiskit
```

---

