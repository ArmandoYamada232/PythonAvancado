print('Insira o valor dos preços dos produtos para obter a média')
soma = 0
media = 0
lista = []
for count in range (2):
    preco = float(input('Insira o valor do produto: '))
    if preco < 0:
        print('Valor inválido!')
    else:
        lista.append(preco)
        soma += preco
        media = soma / 2
print(f'A média dos produtos é: {media:.2f}')
print(lista)