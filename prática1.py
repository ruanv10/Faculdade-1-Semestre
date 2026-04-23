alunos = []

x = int(input('Digíte a quantidade de aluno: '))
for i in range (5):
    nome = input(F'Digíte o nome do {i+1} aluno: ').capitalize()
    nota = float(input(f'Digíte a nota do aluno(a) {nome}: '))
    alunos.append((nome, nota))