from rich import print
from rich.panel import Panel


class Gamer:
    def __init__(self, nome: str, nick: str):
        self.nome = nome
        self.nick = nick
        self.jogos_fav = []

    def adicionar_jogos(self):
        jogo = str(input('Digite o nome do jogo: '))
        self.jogos_fav.append(jogo)

    def mostrar_ficha(self):
        perfil = Panel(f'Nome real: {self.nome}\njogos favoritos: {",".join(self.jogos_fav)}', title=self.nick)
        return perfil


gamer1 = Gamer('Armando', 'Robochoices')
gamer1.adicionar_jogos()
gamer1.adicionar_jogos()
gamer1.adicionar_jogos()
print(gamer1.mostrar_ficha())
