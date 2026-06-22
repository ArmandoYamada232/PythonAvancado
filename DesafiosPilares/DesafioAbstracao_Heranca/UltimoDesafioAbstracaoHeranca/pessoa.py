from abc import ABC
from datetime import datetime


class Pessoa(ABC):
    def __init__(self, nome: str, nascimento: int):
        self._nome = nome
        self._nascimento = nascimento
        self._idade = 0

    @property
    def nascimento(self):
        return self._nascimento

    @nascimento.setter
    def nascimento(self, data: int):
        ano_atual = datetime.now().year
        if data > ano_atual or data < 1900:
            raise ValueError('Data inválida!')
        else:
            self._idade = ano_atual - data
