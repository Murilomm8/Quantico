import os
import sys

print("🔍 Diagnóstico do ambiente Qiskit\n")

# 1. Verificar se o ambiente virtual está ativado
venv_path = sys.prefix
print(f"📦 Ambiente virtual ativo: {venv_path}")

# 2. Verificar variável de ambiente
symengine_flag = os.environ.get("QISKIT_SYMENGINE", "❌ Não definida")
print(f"⚙️ QISKIT_SYMENGINE = {symengine_flag}")

# 3. Testar importação do Qiskit
try:
    from qiskit import QuantumCircuit
    from qiskit.primitives import Sampler
    print("✅ Qiskit importado com sucesso")
except ImportError as e:
    print("❌ Erro ao importar Qiskit:", e)
    sys.exit(1)
except ModuleNotFoundError as e:
    print("❌ Módulo ausente:", e)
    sys.exit(1)

# 4. Testar execução de um circuito simples
try:
    qc = QuantumCircuit(1)
    qc.h(0)
    qc.measure_all()

    sampler = Sampler()
    result = sampler.run(qc).result()
    counts = result.quasi_dists[0]

    print("✅ Simulação executada com sucesso")
    print("📊 Resultados:", counts)
except Exception as e:
    print("❌ Erro ao executar simulação:", e)
