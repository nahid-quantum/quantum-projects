from hamiltonian import build_h2_hamiltonian
from ansatz import build_ansatz
from optimizer import optimize_energy
import matplotlib.pyplot as plt

def main():
    H, num_qubits = build_h2_hamiltonian()
    ansatz, params = build_ansatz(num_qubits)
    energies, result = optimize_energy(H, ansatz, params)

    print("Final Ground State Energy:", energies[-1])

    plt.plot(energies)
    plt.xlabel("Iteration")
    plt.ylabel("Energy (Hartree)")
    plt.title("VQE Energy Convergence")
    plt.savefig("results/energy_plot.png")

if __name__ == "__main__":
    main()