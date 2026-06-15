#Declaração de classe
class pessoa:
    def __init__(self): # Metodo construtor
        #atributo de instancia
        self.nome = ''
        self.idade = 0

    # metodos de instancia
    def aniversario(self):
            self.idade = self.idade + 1
            self.idade +=1 #self = idade +1

    def mensagem(self):
        return f'{self.nome} tem a idade de {self.idade} anos'

#instanciar objeto
p1 = pessoa()
p1.nome = 'Armando'
p1.idade = 23
print(p1.nome)
print(p1.idade)
print(p1.mensagem())