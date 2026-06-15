class Avaliacao:
    def __init__(self, nome, disciplina, nota=0):
        self.nome = nome
        self.disciplina = disciplina
        self._nota = nota

    # Atributos validados
    @property
    # Atributo nota diferenciado validável para mexer em _nota
    def nota(self):
        return self._nota

    # pega a variavel diferenciada e coloca @variavel.setter
    @nota.setter
    def nota(self, valor):
        if 0 <= valor <= 10:
            self._nota = valor
        else:
            print('Nota inválida')
