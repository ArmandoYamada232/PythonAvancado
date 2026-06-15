import math
def teste ():
    numero = int(input('Insira um numero: '))
    palavra = str(input('Insira uma palavra: '))

    print(f'O número é: {numero}',type(numero))
    print(f'A palavra é: {palavra}',type(palavra))

def saudacao ():
    print('Bem vindo(a)')

def cubo (num):
    result = num * num * num
    result2 = num **3
    #Utilizando a biblioteca math importando o pow(x,y) para potenciação
    #(função)pow(num,y que é o número da potenciação
    result3 = pow(num,3)

    print(f'{num} x {num} x {num} = {result}')
    print(f'{num} x {num} x {num} = {result2}')
    print(f'{num} x {num} x {num} = {result3}')


def fatorar ():
    num = int(input('Insira um numero para fatorar: '))
    print(f'O número: {num} fatorado é !={math.factorial(num)}')
