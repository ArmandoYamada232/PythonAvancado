from funcionario import Funcionario
from rich.panel import Panel
from rich.console import Console

console = Console()

class Mensalista(Funcionario):
    def __init__(self, nome, sal_bruto):
        super().__init__(nome, sal_bruto)

    def calc_salario(self):
        desconto = self.sal_bruto * (7.5 / 100)

        valor_inns = self.sal_bruto - desconto

        return valor_inns

    def analisar_salario(self):
        tela = Panel(f'Nome: {self.nome}\n'
                     f'Tipo de funcionário: {self.__class__.__name__}\n'
                     f'salário: {self.calc_salario()}\n'
                     f'Quantidade de salários mínimos: {self.saber_salario_min():.2f}', title='Funcionario')
        console.print(tela)

    def saber_salario_min(self):
        qtd_sal_min = self.sal_bruto / self.salario_min

        return qtd_sal_min
