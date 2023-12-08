pares = []
vetor = [0] * 10


for i in range(10):
    
    vetor[i] = int(input(f"Digite o valor da posição {i}: "))


cont_pares = 0


for valor in vetor:
    if valor % 2 == 0:
        cont_pares += 1
       
        pares.append(valor)

print("No vetor há", cont_pares ,"pares. E os valores pares são:", ', '.join(map(str, pares)))


 

