import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Criação de um dataset fictício
np.random.seed (42)

dados = pd.DataFrame({
    "Orcamento_Campanha": np.random.randint(2000, 5000, size=100),
    "Visualizacoes_Anuncio": np.random.randint(2000, 200000, size=100),
    "Vendas": np.random.randint(10, 5000, size=100),
    "Cliques": np.random.randint(100, 200000, size=100)
})

# Pairplot: Visualizar todas as relações
sns.pairplot(dados)
plt.show()
plt.savefig('pairplot7.png')

# Joinplot: Explorar a relação a relação entre duas variáveis específicas
sns.jointplot(x='Visualizacoes_Anuncio', y='Vendas', data= dados, kind="reg")
plt.show()
plt.savefig('joinplot7.png')

# Lmplot: Visualizar a linha de regressão
sns.lmplot(x= 'Visualizacoes_Anuncio', y='Vendas', data=dados)
plt.show()
plt.savefig('lmplot7.png')