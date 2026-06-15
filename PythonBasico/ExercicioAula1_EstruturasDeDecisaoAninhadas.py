from math import sqrt

print('Insira os valores de A, B, C para fazer o cálculo da equação de segundo grau')
a = int(input('Insira o valor de A: '))
b = int(input('Insira o valor de B: '))
c = int(input('Insira o valor de C: '))

if a == 0:
    print('Equação inválida')
else:
    delta = b**2 - 4*a*c
    print(f'O Delta é: {delta}')
    if delta < 0:
        print('A Equação não possui raizes')
    elif delta == 0:
        x = (-b + sqrt(delta))/(2*a)
        print(f'Possui apenas um x = {x:.2f}')
    elif delta > 0:
        x1 = (-b + sqrt(delta))/(2*a)
        x2 = (-b - sqrt(delta))/(2*a)
        print('Possui x1 e x2')
        print(f'x1 = {x1:.2f}')
        print(f'x2 = {x2:.2f}')

input('pressione enter para sair')
