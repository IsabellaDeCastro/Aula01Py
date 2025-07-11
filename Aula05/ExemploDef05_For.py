# Conatadores utilizando o For


def contador ():
    for i in range(11):
      print(i)
    
def contador_2 ():
    for i in range (0, 11, 2):
      print(i)
    
alunos = ["Isa","Bella", "Matheus", "Nicollas"]

def Boanoite():

  for i in alunos:
    print(f"Boa noite {i}")
 

print("Contador 1 ao 10:")   
contador()

print("Contador pulando de 2 em 2:")
contador_2()

print("Mensagem de boa noite:")
Boanoite()