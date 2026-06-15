from datetime import datetime
from abc import ABC, abstractmethod #Abstract Base classes

class Pessoa (ABC):
    def __init__(self, nome, data_nas, cpf):
        self.nome = nome
        self.data_nasc = data_nas
        self.cpf = cpf

    def fazer_aniversario(self):
        ano_atual = datetime.today().year
        idade = ano_atual - self.data_nasc
        return f'Parabéns, você fez aniversario e a sua idade é: {idade} anos.'


    def apresentar(self):
        return f'Olá meu nome é: {self.nome}, minha idade é {self.fazer_aniversario()}'

    @abstractmethod
    def estudar(self):
        pass 