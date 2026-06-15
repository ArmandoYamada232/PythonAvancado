from abc import ABC, abstractmethod
from rich import print


class Bebida(ABC):
    def __init__(self):
        pass

    def preparar(self):
        print(f'Bebida: {self.__class__.__name__}')
        self.ferver_agua(),
        self.misturar(),
        self.servir()
        print(1*'\n')

    def ferver_agua(self):
        print('Fervendo água a 100 graus celcius')

    @abstractmethod
    def misturar(self):
        pass

    @abstractmethod
    def servir(self):
        pass
