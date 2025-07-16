# importa a biblioteca de graficos 
import matplotlib.pyplot as plt

#dados para o grafico
marcas = ['Motorala', 'Samsung', 'Apple','Xiaomi']
quantidade = [80, 65, 40, 90]

#Criar o grafico de barras 
plt.bar( marcas , quantidade)

#Adiciona titulo e rotulos
plt.title("Celulares mais usados")
plt.xlabel("Marcas")
plt.ylabel("Quantidade")

# mostrar o grafico na tela
plt.show()