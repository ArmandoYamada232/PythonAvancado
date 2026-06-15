from abc import ABC, abstractmethod
from rich.table import Table


class Transporte(ABC):
    def __init__(self, distancia):
        self.distancia = distancia

    @abstractmethod
    def calc_frete(self):
        pass

    def gerar_tabela(self):
        tabela = Table(title='Tabela de preços do frete')

        tabela.add_column('Veículo')
        tabela.add_column('Distancia')
        tabela.add_column('Frete')

        tabela.add_row(self.__class__.__name__, str(self.distancia, f'{self.calc_frete():.2f}'))

        print(tabela)
