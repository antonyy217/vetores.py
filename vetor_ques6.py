num = [0] * 8

inicio = input('Você irá dizer 8 valores e logo após falar 2 posições desses 8 valores \n para somar eles (pressione OK para continuar): ')

if inicio == 'ok' or 'OK':
 
 for i in range(8):
  num[i] = float(input(f'Diga o número da posição {i}: '))

 
 print(f'\n {num}')
 print()

 x = int(input('Diga qualquer posição (lembrando que vai de 0 a 8): '))
 print()
 print(f'posição = {x} \nnúmero correspondente a posição = {(num[x])} ' )
 print()

 y = int(input('Diga qualquer posição (lembrando que vai de 0 a 8): '))
 print()
 print(f'posição = {y} \nnúmero correspondente a posição = {(num[y])} ' )
 print()

 
 
 print()
 print (f'{(num[x])} + {(num[y])} = {(num[x]) + (num[y])}' )