from rich import print


class Caneta:
    def __init__(self):
        self.caneta_azul = 'Azul'
        self.caneta_verde = 'Verde'
        self.caneta_preta = 'Preta'
        self.cor_invalida = 'Invalida'
        self.mensagem = ''
        self.cor = None

    def destampar_caneta(self):
        self.cor = str(input('Insira a cor da caneta: '))
        if self.cor == 'Azul'.lower().strip():
            print('[blue]você destampou a caneta azul[/]')
            return self.caneta_azul
        elif self.cor == 'Verde'.lower().strip():
            print('[green]Você destampou a caneta verde[/]')
            return self.caneta_verde
        elif self.cor == 'Preta'.lower().strip():
            print('[black]Você destampou a caneta preta[/]')
            return self.caneta_preta
        else:
            print('Cor invalido')
            return self.cor_invalida

    def escrever(self):
        self.mensagem = str(input('Insira uma mensagem: '))
        if self.cor == 'Azul'.lower().strip():
            print(f'[blue]{self.mensagem}[/]')
        elif self.cor == 'Verde'.lower().strip():
            print(f'[green]{self.mensagem}[/]')
        elif self.cor == 'Preta'.lower().strip():
            print(f'[black]{self.mensagem}[/]')

"""caneta1 = Caneta()
caneta1.destampar_caneta()
caneta1.escrever()"""

caneta2 = Caneta()
caneta2.destampar_caneta()
caneta2.escrever()

