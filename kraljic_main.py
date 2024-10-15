import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Exemplo de série temporal com preços e volumes de compra
# Substitua por sua própria série temporal
data = {
    'Produto': ['A', 'B', 'C', 'D'],
    'Preco_Medio': [100, 150, 200, 50],
    'Volatilidade': [0.1, 0.4, 0.3, 0.2],  # Volatilidade de preços
    'Impacto_Financeiro': [5000, 8000, 3000, 2000]  # Valor total gasto
}

df = pd.DataFrame(data)

# Definindo o eixo de Impacto Financeiro e Risco de Suprimento
impacto_financeiro = df['Impacto_Financeiro']
risco_suprimento = df['Volatilidade']

# Criar gráfico da Matriz Kraljic
plt.figure(figsize=(8, 8))
plt.scatter(risco_suprimento, impacto_financeiro, s=100)

# Adicionar rótulos aos pontos
for i, produto in enumerate(df['Produto']):
    plt.text(risco_suprimento[i], impacto_financeiro[i], produto, fontsize=12)

# Definir limites dos eixos
plt.xlim(0, 1)  # Limites para risco de suprimento
plt.ylim(0, 10000)  # Limites para impacto financeiro

# Adicionar títulos e rótulos dos eixos
plt.title('Matriz Kraljic')
plt.xlabel('Risco de Suprimento')
plt.ylabel('Impacto no Negócio')

# Adicionar linhas para separar os quadrantes
plt.axhline(y=5000, color='black', linestyle='--')  # Linha horizontal para separar alto e baixo impacto
plt.axvline(x=0.3, color='black', linestyle='--')  # Linha vertical para separar alto e baixo risco

# Exibir o gráfico
plt.grid(True)
plt.show()
