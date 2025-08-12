import os
os.environ["QISKIT_SYMENGINE"] = "False"

from qiskit import QuantumCircuit
from qiskit.primitives import Sampler
import matplotlib.pyplot as plt

# Circuito: Hadamard + CNOT + Medição
qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
qc.measure_all()

# Executar com Sampler
sampler = Sampler()
result = sampler.run(qc).result()
counts = result.quasi_dists[0]

# Mostrar resultados
print("Contagens simuladas:", counts)

# Visualizar com Matplotlib
plt.bar(counts.keys(), counts.values(), color='mediumslateblue')
plt.xlabel("Estados")
plt.ylabel("Probabilidade")
plt.title("Resultado da Simulação Quântica")
plt.grid(True)
plt.show()
