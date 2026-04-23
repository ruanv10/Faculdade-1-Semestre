nomes = []
notas = []
x = int(input('Digíte a quantidade de aluno: '))
for i in range (5):
    nome = input(F'Digíte o nome do {i+1} aluno: ').capitalize()
    nota = float(input(f'Digíte a nota do aluno(a) {nome}: '))
    nomes.append(nome)
    notas.append(nota)
    
while True:
    n = int(input(f'Digite o indíce do aluno (0 - {x-1}): '))
    if n >= 0 and n < (x-1): break
    else: print('Digite o valor válido')
    
print(f'A nota do aluno {nomes[n]} é {notas[n]}')

nome = input('Digite o nome do aluno: ')
if nome in nomes:
    indice = nomes.index(nome)
    print(f'A nota do aluno {nomes[indice]} é {notas[indice]}')
else:
    print('Aluno não encontrado!!')