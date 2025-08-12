🧠 Projeto Quantico com Qiskit
Este projeto demonstra um circuito quântico simples utilizando o Qiskit, com visualização dos resultados em gráfico de barras. Ideal para quem está começando na computação quântica e quer entender superposição, entrelaçamento e medição.

📦 Requisitos
Windows 64-bit

Python 3.10 instalado

Ambiente virtual com Qiskit 0.43.0

Matplotlib para visualização

⚙️ Instalação
1. Clone ou crie a pasta do projeto
bash
mkdir E:\projetos\quantico
cd E:\projetos\quantico
2. Crie o ambiente virtual com Python 3.10
bash
py -3.10 -m venv qiskit-py10
.\qiskit-py10\Scripts\activate
3. Instale os pacotes necessários
bash
pip install --upgrade pip
pip install "qiskit==0.43.0" matplotlib
🧪 Execução
Crie o arquivo main.py com o seguinte conteúdo:

python
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
Execute com:

bash
python main.py
✅ Resultado Esperado
Saída no terminal com os estados simulados (ex: {'00': 0.49, '11': 0.51})

Gráfico de barras mostrando a distribuição de probabilidades

🧠 Conceitos Demonstrados
Superposição: Porta Hadamard no qubit 0

Entrelaçamento: Porta CNOT entre qubit 0 e 1

Medição: measure_all() para observar os estados

Execução: Usando Sampler, novo método do Qiskit 1.x

Visualização: Gráfico com Matplotlib
