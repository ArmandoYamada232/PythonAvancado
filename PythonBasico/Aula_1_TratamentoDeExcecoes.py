while True:
    try:
        print('Divisão de numeros')
        n1 = int(input('Digite um numero: '))
        n2 = int(input('Digite outro numero: '))
        result = n1 / n2
        print(f'O Valor de {n1}/{n2} = {result:.2f} ')
        break
    except ValueError as e:
        print(e)
    except ZeroDivisionError as e:
        print('erro: ', type(e))

