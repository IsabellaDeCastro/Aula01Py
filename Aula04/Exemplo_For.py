# Contador utilizando o FOR
# Com ele você define quantas vezes ele vai se repetir

# range() cria uma sequencia de numeros

for contadora in range (3):
    print("contando..", contadora)


# para criar e fazer ele pular, é só adicionar um terceiro valor

for contadora in range(1, 22, 10):
    print(contadora)
    
   
    
# ou dessa forma, declarando as variaveis antes:

inicio = 2 
fim = 51
passo = 10

for contadora in range(inicio, fim, passo):
    print(contadora)