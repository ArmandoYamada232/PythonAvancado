# Declaração de classe
class pessoa:
    '''
    Para colocar manual é só colocar 3 aspas embaixo da classe e será criado o docString
    peps são boas recomendações de praticas com python lá da ver como escrever melhores docStrings
    '''

    def __init__(self, nome='null', idade=0):  # Metodo construtor
        # atributo de instancia
        # esse primeiro nome é o atributo da instancia
        self.nome = nome  # valor que veio do parametro do metodo build
        self.idade = idade

    # metodos de instancia
    def aniversario(self):
        self.idade = self.idade + 1
        self.idade += 1  # self = idade +1

    def mensagem(self):
        return f'{self.nome} tem a idade de {self.idade} anos'

    def __str__(self):
        return f'{self.nome} tem {self.idade} anos'

    def __getstate__(self):
        return f'Estado = {self.nome} e idade = {self.idade}'
# instanciar objeto
p1 = pessoa('Armando', 23)
print(p1.mensagem())

p2 = pessoa()
print(p2.mensagem())

print(p1.__doc__)  # Dunder Attribute
print(p1.__dict__) # Dunder Dicionario mostra em forma de dicionario
print(p1.__getstate__()) # dunder metodo que mostra em forma de dicionario
print(p1.__class__) # para saber a classe do objeto
