from classe_abstrata_poligono import Poligono

class Quadrado (Poligono):
    def __init__(self, comprimento_lado):
        super().__init__(4)
        self.comprimento_lado = comprimento_lado


    def calc_area(self):
        area = self.comprimento_lado **2
        print(f'A área do quadrado é: {area}')

    def calc_perimetro(self):
        perimetro = 4 * self.comprimento_lado
        print(f'O perimetro do quadrado é: {perimetro}\n')
