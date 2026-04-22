import random
import time

def mostra_senha(indice, digitos):
    if indice == 0:
        return '____'
    elif indice == 1:
        return f'{digitos[0]}___'
    elif indice == 2:
        return f'{digitos[0]}{digitos[1]}__'
    elif indice == 3:
        return f'{digitos[0]}{digitos[1]}{digitos[2]}_'
    else:
        return f'{digitos[0]}{digitos[1]}{digitos[2]}{digitos[3]}'

# Gera senha de 4 dígitos (como string)
digitos = str(random.randint(0, 9999)).zfill(4)
indice = 0
tentativa = 0
inicio = time.time()


# Implementar o núcleo do código aqui
while indice < 4:
    
    chute = input(f'Digte o seu chute {indice+1} digíto: ')
    
    if chute < digitos[indice]:
        print('O digíto é Maior!')
    elif chute > digitos[indice]:
        print('O digíto é Menor!')
    else:
        print('Digíto está correto!')
    
        indice += 1
        tentativa += 1
        tempo_total = time.time () - inicio

print("n Cofre aberto com sucesso!")
print(f"Senha: {digitos}")
print(f"Tentativas: {tentativa}")
print(f"Tempo: {tempo_total:.2f} segundos")