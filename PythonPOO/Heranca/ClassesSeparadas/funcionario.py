from pessoa import Pessoa


class Funcionario(Pessoa):
    def __init__(self, nome, data_nas, cpf, cargo, setor, id_funcionario):
        super().__init__(nome, data_nas, cpf)
        self.cargo = cargo
        self.setor = setor
        self.id_funcionario = id_funcionario

    def bater_ponto(self):
        return f'O Funcionário com nome de {self.nome} e id: {self.id} bateu o ponto.'

