from classe_abstrata_bebida import Bebida


class Cafe(Bebida):
    def __init__(self):
        super().__init__()

    # Metodos abstratos

    def misturar(self):
        print('Passando água pressurizada pelo café moído ')

    def servir(self):
        print('Servir em xícara pequena')
