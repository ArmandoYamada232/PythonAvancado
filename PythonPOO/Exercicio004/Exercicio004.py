class Pessoa:
    def __init__(self,nome = '', idade = 0):
        self.nome = nome
        self.idade = idade


    def fazer_aniversaio(self):
        self.idade = self.idade+1

#Usa dentro do parentese a Super classe
class Aluno(Pessoa):
    def __init__(self,nome, idade, curso, turma):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma

    def fazer_matricula(self):
        pass

class Professor(Pessoa):
    def __init__(self, nome, idade,especialidade, nivel):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel

    def dar_aula(self):
        pass

class Funcionario(Pessoa):
    def __init__(self,nome,idade, cargo, setor):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor
        
    def bater_ponto(self):
        pass