import numpy as np
from scipy import stats

# Notas de matemática
notas = [78, 85, 91, 73, 88, 92, 79, 85, 90, 87]

# Calcular média
media = np.mean(notas)
print(f'Média: {media}')

# Calcular a moda
moda = stats.mode(notas, keepdims=True)
print(f'Moda: {moda.mode[0]}, Frequência: {moda.count[0]}')