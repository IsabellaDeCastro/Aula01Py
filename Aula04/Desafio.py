
# Desafio criar um programa para pedir 3 nomes, guardar em uma lista e dar boa noite para eles

print("Programa crie sua lista")

nomes = []

for i in range(3):
    nomes.append(input("Digite um nome:"))
print(nomes)
    
for i in nomes:
    print(f"Boa noite{i}!")
    


