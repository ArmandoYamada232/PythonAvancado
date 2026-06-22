from DesafiosPilares.DesafioAbstracao_Heranca.UltimoDesafioAbstracaoHeranca.pessoa import Pessoa
from rich import inspect


class Aluno(Pessoa):
    def __init__(self, nome, nascimento, curso: str):
        super().__init__(nome, nascimento)
        self._curso = curso
        self.cursos_oficiais = ['ENG', 'ADM', 'AGRO']

        if curso in self.cursos_oficiais:
            print()
        else:
            raise ValueError('Curso não encontrado')

    @property
    def add_cursos(self):
        return self.cursos_oficiais

    @add_cursos.setter
    def add_cursos(self, nome_curso):
        if nome_curso != '' and nome_curso != ' ':
            self.cursos_oficiais.append(nome_curso)
        else:
            raise ValueError('Valor inválido')


a1 = Aluno('Armando', 2002, 'ADM')
a1.add_cursos = 'GEO'
a1.nascimento = 1910
inspect(a1, methods=True, private=True)
