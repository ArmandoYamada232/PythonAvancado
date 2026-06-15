from rich import print


class Caneta:
    def __init__(self):
        self.caneta_azul = 'Azul'
        self.caneta_verde = 'Verde'
        self.caneta_preta = 'Preta'
        self.cor_invalida = 'Invalida'

    def destampar_caneta(self):
        cor = str(input('Insira a cor da caneta: '))

        if cor == 'Azul'.lower().strip():
            print('[blue]você destampou a caneta azul[/]')
            return self.caneta_azul
        elif cor == 'Verde'.lower().strip():
            print('[green]Você destampou a caneta verde[/]')
            return self.caneta_verde
        elif cor == 'Preta'.lower().strip():
            print('[black]Você destampou a caneta preta[/]')
            return self.caneta_preta
        else:
            print('Cor invalido')
            return self.cor_invalida

caneta = Caneta()
caneta.destampar_caneta()
