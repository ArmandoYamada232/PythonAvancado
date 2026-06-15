print('Advinhe o número')
while True:
    numero = int(input('Digite um numero de 1 a 10: '))
    if numero < 0:
        print(f'O número que você escolheu é negativo! número: {numero}')
        continue
    if numero != 7:
        print(f'Continue tentando o numero ({numero}) que você escolheu não foi o sorteado')
        continue
    else:
        print(f'Parabens você encontrou o número sorteado numero: {numero}')
        break
