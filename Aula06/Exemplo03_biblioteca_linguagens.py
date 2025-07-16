# importa a biblioteca de graficos 
import matplotlib.pyplot as plt

#dados para o grafico
categorias = ['Python', 'JavaScript', 'Java']
quantidade = [80, 65, 40]

#Criar o grafico de barras 
plt.bar(categorias, quantidade)

#Adiciona titulo e rotulos
plt.title("Linguagens mais usadas")
plt.xlabel("Linguagem")
plt.ylabel("Quantidade")

# mostrar o grafico na tela
plt.show()