import numpy as np
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

def quantum_predict(X):
    simulator = AerSimulator()
    preds = []

    for x in X:
        qc = QuantumCircuit(2, 2)

        angle = x[0]

        # Feature encoding
        qc.ry(angle, 0)
        qc.rx(angle, 1)

        # More expressive circuit
        qc.cx(0, 1)
        qc.ry(angle/2, 0)
        qc.cx(1, 0)

        qc.measure([0,1], [0,1])

        result = simulator.run(qc, shots=2000).result()
        counts = result.get_counts()

        prob_11 = counts.get('11', 0) / 2000

        # Tuned threshold
        preds.append(1 if prob_11 > 0.25 else 0)

    return np.array(preds)