import pandas as pd
import numpy as np

# Exemplo de preços históricos de um ativo (você pode substituir por seus dados)
data = {
    'Date': ['2024-10-01', '2024-10-02', '2024-10-03', '2024-10-04', '2024-10-05'],
    'Price': [100, 102, 101, 105, 104]
}
df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

# 1. Calcular os retornos logarítmicos diários
df['Log_Returns'] = np.log(df['Price'] / df['Price'].shift(1))

# 2. Calcular a volatilidade diária (desvio padrão dos retornos logarítmicos)
volatility_daily = df['Log_Returns'].std()

# 3. Anualizar a volatilidade (multiplicando pela raiz quadrada de 252 dias úteis)
volatility_annual = volatility_daily * np.sqrt(252)

# Exibir o resultado
print(f'Volatilidade anualizada: {volatility_annual:.4f}')
