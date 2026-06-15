import random

from personagem import Personagem


class Guerreiro(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ['soco', 'investida', 'chute na cabeça']

    def curar(self):
        cura = random.randint(0, 150)
        self.vida = self.vida + cura
        print(f'Personagem {self.nome} se curou com atadura {cura} pontos de vida'
              f'e está com a vida: {self.vida}')
