import datetime

def votar():
    print('Cheque se você pode votar.')
    data_nascimento = str(input('Data de nascimento: '))
    data_nascimento = datetime.datetime.strptime(data_nascimento, '%Y-%m-%d')
    ano = datetime.date.today().year
    idade = ano - data_nascimento.year
    print(f'A idade é: {idade} anos')

    if idade >= 18:
        print(f'Sua idade é {idade} e seu voto é Obrigatorio')
    elif (idade >= 16) and (idade <= 17):
        print(f'Você tem apenas {idade} e o seu voto é opcional')
    else:
        print(f'Voto é negado,porque você tem {idade}')

votar()