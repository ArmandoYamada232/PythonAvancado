import re


def receber_nome_salario():
    while True:
        nome = str(input('Digite seu nome: ')).strip()
        padrao = r'^[A-Za-zÀ-ÿ]+( [A-Za-zÀ-ÿ]+)*$'
        if re.match(padrao, nome):
            break
        else:
            print('Nome inválido tente novamente')

    while True:
        try:
            salario = float(input('Insira o salário: '))

            if salario <= 0:
                print('Salário não pode ser zero nem negativo')
                continue

            break

        except ValueError:
            print('Erro coloque apenas números')

    return nome, salario


receber_nome_salario()
