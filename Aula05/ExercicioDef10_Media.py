# Calcular a média entre 3 valores 

print("Programa para calcular a média entre 3 valores")

def media (numero1,numero2,numero3):
    media = (numero1 + numero2 + numero3) / 3
    print (f"A média entre os 3 valores é: {media}")

numero1 = int(input("Digite um número:")) 
numero2 = int(input("Digite o segundo número:"))
numero3 = int(input("Digite um terceiro número:"))

media(numero1, numero2, numero3)


    