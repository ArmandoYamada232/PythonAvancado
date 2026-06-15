from funcionario import Funcionario


class Professor(Funcionario):
    def __init__(self,nome, data_nas,cpf, especialidade, nivel, cargo, setor, id_funcionario):
        super().__init__(nome,data_nas,cpf, cargo,setor,id_funcionario)
        self.especialidade = especialidade
        self.nivel = nivel


    def dar_aula(self):
        return f'Professor: {self.nome}'

    def estudar(self):
        print(f'Professor {self.nome}, nivel: {self.nivel} com a especialidade em: {self.especialidade} ')
