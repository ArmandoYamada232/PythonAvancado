def ler_preco():
    lista = []
    for cont in range(2):
        preco = float(input('Insira o valor do produto: '))
        if preco < 0:
            print('Valor Inválido, digite outro valor')
        else:
            lista.append(preco)

    return lista


def calcular_preco(lista):
    if not lista:
        print('Lista está vazia')
        return 0
    soma = 0
    for preco in lista:
        soma += preco
    return soma

def calc_media_preco(lista):
    if not lista:
        return 0
    return calcular_preco(lista)/len(lista)

def main():
    print('Sistema de preços')
    total = ler_preco()
    media = calc_media_preco(total)

    print(total)
    print(media)

if __name__ == '__main__':
    main()





