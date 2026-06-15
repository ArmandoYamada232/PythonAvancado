from abc import ABC, abstractmethod
from rich import print
# from rich.panel import Panel
import random


class Personagem(ABC):
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida
        self.golpes = []

    def mostrar_personagem(self):
        print(f'Nome: {self.nome}, vida: {self.vida}')

    def atacar(self, alvo, forca = 50):
        if self.vida > 0 and alvo.vida > 0:
            golpe = self.golpes[random.randrange(0, len(self.golpes))]
            print(f'{self.nome} atacou {alvo.nome} com um golpe {golpe}')
            alvo.receber_dano(forca)
        else:
            print(f'O ataque contra o {self.nome} não poderá ocorrer!')

    def receber_dano(self, dano):
        fator = random.randint(1, dano)
        self.vida -= fator
        if self.vida <= 0:
            self.vida = 0
        print(f'Personagem: {self.nome} recebeu {fator} de dano.')

    @abstractmethod
    def curar(self):
        pass
