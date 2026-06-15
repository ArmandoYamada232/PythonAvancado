from funcionario import Funcionario
from rich.panel import Panel
from rich.console import Console

console = Console()

class Horista(Funcionario):
    def __init__(self, nome, valor_hora, horas_trab):
        sal_bruto = valor_hora * horas_trab
        super().__init__(nome, sal_bruto)
        self.valor_hora = valor_hora
        self.horas_trab = horas_trab

    def analisar_salario(self):
        tela = Panel(f'Nome: {self.nome}\n'
                     f'Tipo de funcionário: {self.__class__.__name__}\n'
                     f'salário: {self.calc_salario()}\n'
                     f'Quantidade de salários mínimos: {self.saber_salario_min():.2f}', title='Funcionario')
        console.print(tela)

    def calc_salario(self):
        desconto = self.sal_bruto * (7.5/100)
        return self.sal_bruto - desconto

    def saber_salario_min(self):
        sal_mensal = self.valor_hora * self.horas_trab
        qtd_sal = sal_mensal / Funcionario.salario_min
        return qtd_sal

