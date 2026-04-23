alunos = [] 
soma = 0

x = int(input('Digíte a quantidade de aluno: '))
for i in range(x):
    nome = input(F'Digíte o nome do {i+1}º aluno: ').capitalize()
    nota = float(input(f'Digíte a {i+1}º nota do aluno(a) {nome}: '))
    nota2 = float(input(f'Digíte a {i+2}º nota do aluno(a) {nome}: '))
    alunos.append((nome, nota, nota2))
    soma += nota, nota2
    
media = soma/len(nota, nota2)
print(f'A média é: {media:.2f}')