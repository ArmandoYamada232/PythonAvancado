from DesafiosPilares.DesafioAbstracao_Heranca.Desafio001.classe_circulo import Circulo
from DesafiosPilares.DesafioAbstracao_Heranca.Desafio001.classe_quadrado import Quadrado


def main():
    poligono1 = Quadrado(12)
    poligono1.calc_area()
    poligono1.calc_perimetro()

    poligono2 = Circulo(20)
    poligono2.calc_area()
    poligono2.calc_perimetro()


if __name__ == '__main__':
    main()
