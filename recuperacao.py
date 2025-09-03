import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Vendas em ordem crescente
Vendas = [120, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250]

# Calcular quartis
quartis = np.percentile(Vendas, [25, 50, 75])
print(f'Quartis: Q1={quartis[0]}, Q2={quartis[1]}, Q3={quartis[2]}')

# Calcular decis
decis = np.percentile(Vendas, [10, 20, 30, 40, 50, 60, 70, 80, 90])
print(f'Decis: {decis}')

# Calcular percentis
percentis = np.percentile(Vendas, [10, 25, 50, 75, 90])
print(f'Percentis: {percentis}')

# Visualização por BoxPlot
plt.boxplot(Vendas, vert=False)
plt.title('Boxplot das Vendas')
plt.xlabel('Vendas')
plt.show()
plt.savefig('chart6.png')