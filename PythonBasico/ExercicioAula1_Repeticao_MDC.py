print('Diga dois números')

n1 = int(input('Insira o n1: '))
n2 = int(input('Insira o n2: '))

n1, n2 = abs(n1), abs(n2)

if n1 < 1 or n2 < 1:
    print('Não pode ser MCD')
else:
    while True:
        resto = n1 % n2
        print(f'{n1}/{n2} = {resto}')
        if resto == 0:
            break
        n1, n2 = n2, resto
        print(n2)
