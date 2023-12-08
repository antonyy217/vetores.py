vetor = [0] * 6

for i in range(6):
    vetor[i] = int(input(f'Diga o número inteiro da posição {i}: '))


vetor.reverse()

print(vetor)