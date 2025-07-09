# Funções/comandos do dicionario

cliente = {"nome": "Pascoal","numero": 11943984595,"idade":"21","cpf": 93848855949,"endereço": "rua tito" }

print(cliente)

#tamanho do dicionario:
print(len(cliente))

#mostrar um id especifico do dicionario
print(cliente["endereço"])

#remover um id do dicionario
del cliente["nome"]
print(cliente)
print(len(cliente))

#adicionar um id ao dicionario
cliente["nome"]= "Rosana"
print(cliente)
print(len(cliente))


