from personagem import Personagem
import random

class Mago(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ['Bola de fogo', 'espinho de gelo', 'conjurar nevasca']

    def curar(self):
        cura = random.randint(0, 150)
        self.vida = self.vida + cura
        print(f'Personagem {self.nome} fez um feitiço e curou {cura} pontos de vida'
              f'e está com a vida: {self.vida}')
