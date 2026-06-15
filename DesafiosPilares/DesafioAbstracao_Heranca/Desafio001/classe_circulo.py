from classe_abstrata_poligono import Poligono
from math import pi


class Circulo(Poligono):
    def __init__(self, raio):
        super().__init__(0)
        self.raio = raio

    def calc_perimetro(self):
        perimetro = (2 * pi) * self.raio
        print(f'O perimetro do circulo é: {perimetro:.2f}')

    def calc_area(self):
        area = pi * (self.raio ** 2)
        print(f'A área do circulo é: {area:.2f}')
