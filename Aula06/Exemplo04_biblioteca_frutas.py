# importa a biblioteca de graficos 
import matplotlib.pyplot as plt

#dados para o grafico
frutas = ['Maça', 'Pera', 'Uva','Melancia', 'Abacaxi', 'Morango', 'Laranja', 'caqui', 'Banana', 'amora']
quantidade = [80, 65, 40, 30, 35, 20, 10, 9, 84, 90]

#Criar o grafico de barras 
plt.bar(frutas, quantidade)

#Adiciona titulo e rotulos
plt.title("Frutas mais consumidas")
plt.xlabel("Frutas")
plt.ylabel("Quantidade")

# mostrar o grafico na tela
plt.show()