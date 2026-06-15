nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2)/2

if media >= 6:
    print(f'aprovado, com a média de {media} ')
    print('Boas férias')
else:
    print(f'Reprovado, com a média de {media} ')
