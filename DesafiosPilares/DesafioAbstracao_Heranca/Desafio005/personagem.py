from abc import ABC, abstractmethod
from random import randint
from rich import print
from rich.panel import Panel


class Personagem(ABC):
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida
        self.golpes = []

    def atacar(self, alvo, forca):
        dano = randint(1, forca)
        if alvo == self:
            tela1_classe_abstrata = Panel('Você não pode se atacar!')
            print(tela1_classe_abstrata)
        else:
            tela2_classe_abstrata = Panel(f'Você atacou o alvo: {alvo.nome}\n'
                                          f'Classe: {alvo.__class__.__name__}\n'
                                          f'força: {forca}\n'
                                          f'Valor do dano proferido: {dano} pontos.', title='Ataque')
            print(tela2_classe_abstrata)
            alvo.receber_dano(dano)

    def receber_dano(self, dano):
        fator = randint(1, dano)
        self.vida = self.vida - fator
        if self.vida > 0:
            tela1_receber_dano = Panel(f'Nome personagem: {self.nome}\n'
                                       f'Classe: {self.__class__.__name__}\n'
                                       f'Recebeu um dano de: {fator}\n'
                                       f'Vida Restante: {self.vida}\n'
                                       , title='Dano Recebido')
            print(tela1_receber_dano)
        else:
            self.morrer()

    def mostrar_personagem(self):
        tela1_mostrar_personagem = Panel(f'Nome personagem: {self.nome}\n'
                                         f'Classe: {self.__class__.__name__}\n',
                                         title='Card do Personagem')
        print(tela1_mostrar_personagem)

    def morrer(self):
        if self.vida <= 0:
            tela_morte = Panel(f'Personagem:{self.nome}\n'
                               f'Classe: {self.__class__.__name__}\n'
                               f'Status: Morto', title='Morte')
            print(tela_morte)

    @abstractmethod
    def curar(self):
        pass
