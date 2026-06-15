from personagem import Personagem
from random import randint
from rich import print
from rich.panel import Panel

class Mago(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ['Bola de fogo', 'Espinho de gelo', 'conjurar dremora']

    def curar(self):
        cura = randint (0, 300)
        self.vida = self.vida + cura

        tela1_cura_mago = Panel(f'O Mago utilizou feitiço de cura e se curou: {cura} pontos de vida\n'
                                     f'Vida atual é: {self.vida}')
        print(tela1_cura_mago)
