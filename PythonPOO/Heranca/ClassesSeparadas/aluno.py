from pessoa import Pessoa


class Aluno(Pessoa):
    def __init__(self, nome, data_nas, cpf, curso):
        super().__init__(nome, data_nas, cpf)
        self.curso = curso

    def assistir_aula(self):
        return f'O Aluno: {self.nome} está assistindo a aula do curso de {self.curso}'


    def estudar(self):
        print(f'O aluno: {self.nome} faz o curso de {self.curso}')