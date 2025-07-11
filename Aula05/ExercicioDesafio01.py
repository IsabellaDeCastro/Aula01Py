# criar um  lista vazia para guardar os números 

numeros = []

# Pede os números até o usuario digitar 'sair'
entrada = input("Digite um número ou 'sair' para parar:")
while entrada != "sair":
    #Converter para inteiro e guardar na lista
    numeros.append(int(entrada))
    #Pede o proximo número
    entrada = input("Digite um número ou 'sair' para parar:")
    
#Mostrar apenas os números pares
print("Números pares digitados")
for numero in numeros:
    if numero % 2 == 0:
        print(numero)