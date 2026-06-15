# URNA ELETRONICA
import re

def cadastro_candidatos():
    while True:
        nome = input('Digite o nome do candidato: ')
        padrao = r'^[A-Za-zÀ-ÿ]+( [A-Za-zÀ-ÿ]+)*$'
        if re.match(padrao, nome):
            break
        else:
            print('nome inválido! Tente novamente')

    while True:
        numero = str(input('Digite o numero do candidato: '))
        if numero.isnumeric() and len(numero) == 2:
            break
        else:
            print('numero invalido! Tente novamente')

    return nome, numero


def dic_candidatos():
    usuarios = {}
    while True:
        nome, numero = cadastro_candidatos()
        if numero in usuarios:
            print('Número já cadastrado!')
        else:
            usuarios[numero] = {
                'nome': nome,
                'votos': 0
            }

            continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()
            if continuar == 'N':
                break

    return usuarios


def iniciar_votacao(dic_candidatos, cadastro_candidatos):
    while True:
        dic_candidatos(cadastro_candidatos)
        voto = input('Insira o número do candidato: ').strip()
        if voto == '':
            print('Voto em branco')
        elif(voto in dic_candidatos):
            voto = voto + dic_candidatos[voto]
        else:
            voto = 'Nulo'

        confirmar = input('Deseja confirmar o voto? [S/N] ').strip().upper()
        if confirmar == 'S':
            print('Voto Confirmado!')
            break

        return voto

iniciar_votacao()








