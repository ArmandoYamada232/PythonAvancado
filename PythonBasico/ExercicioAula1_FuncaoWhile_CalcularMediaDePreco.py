def ler_preco():
    lista = []
    while True:
        preco = float(input('Insira o preço do produto: '))

        if preco < 0:
            print('Digite um valor válido!')
        else:
            lista.append(preco)

        continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()

        if continuar == 'N':
            break
    return lista

def somar_media_preco(lista):
    if not lista:
        return 0
    return (sum(lista))/ len(lista)

if __name__ == '__main__':
    preco = ler_preco()
    media = somar_media_preco(preco)
    for item in preco:
        print(f' preço: {item}', end=' \n')
    print(f'A média dos preços é: {media}')