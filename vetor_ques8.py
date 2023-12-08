

vetor = [0] * 10

for i in range(10):
    vetor[i] = int(input(f'Diga o número inteiro da posição {i}: '))

maior = max(vetor)

posição_maior =  vetor.index(maior)

print()
print()

print(f'O maior número da lista é {maior}\ne o número {maior} está na posição {posição_maior}')

