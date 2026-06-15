# declarar a classe
from datetime import datetime


class Funcionario:
    def __init__(self):
        self.nome = ''
        self.nasc = 0
        self.idade = 0

    # declarar metodos
    def mensagem(self):
        return f'Olá {self.nome}'

    def aniversario(self):
        ano = datetime.today().year
        idade = ano - self.nasc
        print(f'Olá, {self.nome} você nasceu em {self.nasc} e sua idade é {idade} anos')


# declarar objeto
funcionario1 = Funcionario()
funcionario1.nome = 'Armando'  # nome não parenteses depois é atributos
funcionario1.nasc = 2002
funcionario1.aniversario()

funcionario2 = Funcionario()
funcionario2.nome = 'maureco'
funcionario2.nasc = 1930
funcionario2.aniversario()
print(funcionario2.mensagem())