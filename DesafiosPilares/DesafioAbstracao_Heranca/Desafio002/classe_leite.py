from classe_abstrata_bebida import Bebida


class Leite(Bebida):
    def __init__(self):
        super().__init__()

    # Metodos abstratos
    def misturar(self):
        print('Misturando o pó do leite na água pressurizada.')

    def servir(self):
        print('Servir em uma caneca')
