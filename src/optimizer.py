import numpy as np
from qiskit.algorithms.optimizers import COBYLA
from qiskit.primitives import Estimator

def optimize_energy(H, ansatz, params):
    estimator = Estimator()
    optimizer = COBYLA(maxiter=80)

    energies = []

    def energy(theta):
        result = estimator.run(ansatz.bind_parameters(theta), H).result()
        e = result.values[0]
        energies.append(e)
        return e

    x0 = np.random.random(len(params))
    result = optimizer.minimize(energy, x0)

    return energies, result