import re


def receber_usuarios_e_salario():
    while True:
        nome = input('Digite o nome do usuário: ').strip()
        padrao = r'^[A-Za-zÀ-ÿ]+( [A-Za-zÀ-ÿ]+)*$'
        if re.match(padrao, nome):
            break
        else:
            print('Nome Inválido')

    while True:
        try:
            salario = float(input('Insira o salário do usuário: '))
            if salario <= 0 or salario == ' ':
                print('Salário inválido')
                continue
            break

        except ValueError:
            print('Não é permitido letras, apenas números')

    return nome, salario


def colocar_na_tupla():
    usuarios = []
    while True:
        nome, salario = receber_usuarios_e_salario()
        usuarios.append((nome, salario))

        continuar = str(input('Deseja continuar cadastrando usuários? [S/N] ')).strip().upper()

        if continuar == 'N':
            break

    return usuarios

def main():
        usuarios = colocar_na_tupla() #recebe a tupla

        print('\n Usuários cadastrados:')
        for nome, salario in usuarios:
            print(f'Usuário: {nome} / Salario: R$ {salario:.2f}')


if __name__ == '__main__':
    main()