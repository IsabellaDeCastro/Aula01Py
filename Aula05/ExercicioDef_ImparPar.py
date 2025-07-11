# Programa para verificar se é impar ou par, utilizando função e if else

def imparPar (numero):
    resultado = numero % 2
    if (resultado == 0):
        print(" O número é par")
    else:
        print("Impar")
        
numero = int (input("Digite um número"))
imparPar (numero)