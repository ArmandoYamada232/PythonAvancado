from personagem import Personagem
from random import randint
from rich import print
from rich.panel import Panel


class Guerreiro(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ['soco', 'chute','golpe giratório']

    def curar(self):
        cura = randint(0, 250)
        self.vida = self.vida + cura

        tela1_cura_guerreiro = Panel(f'O Guerreiro utilizou a bandagem e se curou: {cura} pontos de vida\n'
                                     f'Vida atual é: {self.vida}')
        print(tela1_cura_guerreiro)
