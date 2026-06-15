from abc import ABC, abstractmethod


class Funcionario(ABC):
    salario_min = 1612
    qtd_sal_min = 0

    def __init__(self, nome, sal_bruto) -> None:
        self.nome = nome
        self.sal_bruto = sal_bruto

    @abstractmethod
    def calc_salario(self):
        pass

    @abstractmethod
    def analisar_salario(self):
        pass

    @abstractmethod
    def saber_salario_min(self):
        pass
