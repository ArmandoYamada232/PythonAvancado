from classe_abstrata_bebida import Bebida


class Cha(Bebida):
    def __init__(self):
        super().__init__()

    # Metodos abstratos

    def misturar(self):
        print('Colocando o saquinho do chá na água pressurizada')

    def servir(self):
        print('Servir em xícara pequena com rodelas de limão e biscoito de maizena')
