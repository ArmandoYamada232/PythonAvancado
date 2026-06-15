# se colocar um asteritico dentro do parametro aceita qualquer quantidade de número
# def contador(*num):


def contador():
    lista = []
    while True:
        num = int(input('Insira o número para adicionar a lista: '))
        if num == 0:
            print('Número Inválido, tente novamente')
        else:
            lista.append(num)

            continuar = str(input('Deseja continuar adicionando números na lista? [S/N] ')).strip().upper().upper()
            if continuar == 'N':
                break

    print(f'números da lista são: {lista}')
    return lista, num

def dobra_lista():
    lista = contador()
    for x in lista:
        print(x)

dobra_lista()
