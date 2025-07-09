
# CNH

print('Programa para saber se pode tirar a CNH')

nome = input('Digite seu nome:')
idade  = int (input('Digite sua idade:'))

if (idade>=18):
    print(f'{nome}, você é de maior, pode tirar a CNH')
    
else:
    print(f'{nome}, você é de menor, não pode tirar CNH')


