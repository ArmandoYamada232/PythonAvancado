from rich import print
class Diario:
    def __init__(self, senha=''):
        self.__senha = senha
        self.segredos = []

    @property
    def escrever(self):
        return self.segredos

    @escrever.setter
    def escrever(self, texto):
        self.segredos.append(texto)

    def ler_diario(self, password):
        if password == self.__senha:
            print(15*'[yellow]=-[/]','[green bold]Diário Liberado![/]',15*'[yellow]-=[/]')
            for segredos in self.segredos:
                print(f'[yellow]Mensagem[/]: [red]{segredos}[/]')
        else:
            raise ValueError('Senha incorreta, tente novamente')
