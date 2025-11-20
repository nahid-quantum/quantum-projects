from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_histogram

def grover_oracle_2qubits():
    oracle = QuantumCircuit(2, name="Oracle")
    oracle.cz(0, 1)
    return oracle

def grover_diffuser_2qubits():
    diffuser = QuantumCircuit(2, name="Diffuser")
    diffuser.h([0, 1])
    diffuser.x([0, 1])
    diffuser.h(1)
    diffuser.cx(0, 1)
    diffuser.h(1)
    diffuser.x([0, 1])
    diffuser.h([0, 1])
    return diffuser

def build_grover_circuit():
    qc = QuantumCircuit(2, 2)
    qc.h([0, 1])
    qc.append(grover_oracle_2qubits(), [0, 1])
    qc.append(grover_diffuser_2qubits(), [0, 1])
    qc.measure([0, 1], [0, 1])
    return qc

def run_grover():
    qc = build_grover_circuit()
    print(qc.draw())
    backend = Aer.get_backend("qasm_simulator")
    job = execute(qc, backend=backend, shots=1024)
    result = job.result()
    counts = result.get_counts()
    print(counts)
    try:
        plot_histogram(counts).show()
    except:
        pass

if __name__ == "__main__":
    run_grover()