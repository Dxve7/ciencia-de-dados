# Faz a importância da biblioteca matplotlib e adiciona um alias (apelido)
# Usar a  linha de comando: python3 -m pip install matplotlib
import matplotlib.pyplot as plt
def exibirGrafico():
    # Definição dos grupos e valores
    grupos = ['A', 'B', 'C']
    valores = [65, 12, 98]

    # Configura um gráfico de barras, onde recebe os grupos, valores
    # E opcionalmente as cores
    plt.bar(grupos, valores, color = ['green', 'blue', 'yellow'])

    # Define o título do gráfico
    plt.title('Gráfico de Barras Simples')

    #Define o títlo do eixo X
    plt.xlabel('Grupos')

    #Define o títlo do eixo Y
    plt.ylabel('GValores')

    #Cria o gráfico
    plt.show()

    #Salva dentro do arquivo de imagem
    plt.savefig('chart.png')
    