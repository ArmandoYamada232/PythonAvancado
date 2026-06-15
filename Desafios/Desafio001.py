from rich import print


class Funcionarios:
    empresa = 'TecSil'

    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo


    def apresentacao(self)-> str:
        return f'Olá meu nome é [blue]{self.nome}[/] trabalho no setor {self.setor} cargo de {self.cargo} da empresa {Funcionarios.empresa}'


funcionario1 = Funcionarios('Ricardo Tec', 'Setor Tec', 'Gerente')
print(funcionario1.apresentacao())
