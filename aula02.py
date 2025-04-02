import matplotlib.pyplot as plt

# Importa a biblioteca de pandas
import pandas as pd

def exibirGrafico():
    # Cria o dataframe
    df = pd.DataFrame({
        "Meses": ['Jan', 'Fev', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez' ],
        "Temperaturas": [29, 31, 30, 28, 27, 25, 21, 24, 27, 28, 29, 33]
    })

    # Redimensionando o gráfico
    plt.figure(figsize=[10.0, 5.0])

    # Criação do gráfico
    plt.plot(df['Meses'], df['Temperaturas'], color="purple")

    # Definição dos títulos
    plt.title("Temperatura média ao longo do tempo")
    plt.xlabel("Mêses")
    plt.ylabel("Temperaturas")

    # Exibindo o gráfico
    plt.show()
    plt.savefig('chart2.png')

    # Exibe no console dados estátisticos
    print(f'Temperaturas: \n{df['Temperaturas'].describe()}')