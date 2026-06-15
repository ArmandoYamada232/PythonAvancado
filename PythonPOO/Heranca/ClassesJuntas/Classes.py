class Pessoa:
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade

    def aniversario(self):
        pass

    def apresentacao(self):
        return f'Olá meu nome é: {self.nome} eu tenho {self.idade} anos!'


class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor

    def bater_ponto(self):
        return f'O Funcionário: {self.nome} bateu o ponto!'


class Professor(Pessoa):
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel

    def iniciar_aula(self):
        return f'O Professor {self.nome} iniciou a aula.'


class Aluno(Pessoa):
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma

    def realizar_atividade(self):
        return f'Aluno {self.nome} realizou a atividade'
