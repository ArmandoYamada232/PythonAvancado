from abc import ABC, abstractmethod


class Poligono(ABC):
    def __init__(self, qtd_lados):
        self.qtd_lados = qtd_lados

    @abstractmethod
    def calc_perimetro(self):
        pass

    @abstractmethod
    def calc_area(self):
        pass
