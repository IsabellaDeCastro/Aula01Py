# Como atualizar uma tupla para tupla

frutas = ("Banana", "Pera", "Maça")

listfrutas = list(frutas)
listfrutas.append("laranja")
listfrutas.insert(0, 'kiwi')
frutas = tuple(listfrutas)
print(frutas)


TuplaNumero = (0, 1,2,3)
listaNumero = list(TuplaNumero)
listaNumero.append (2)
listaNumero.insert(4,1)
listaNumero = remove (2)
TuplaNumero = tuple(listaNumero)
print(tuple(listaNumero))



 