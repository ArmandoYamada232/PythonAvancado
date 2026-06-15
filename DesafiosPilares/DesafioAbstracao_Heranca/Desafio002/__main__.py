from classe_cafe import Cafe
from classe_cha import Cha
from classe_leite import Leite


def main():
    cafe1 = Cafe()
    cafe1.preparar()

    cha1 = Cha()
    cha1.preparar()

    leite1 = Leite()
    leite1.preparar()


if __name__ == '__main__':
    main()
