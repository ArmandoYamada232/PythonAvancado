from drone import Drone
from caminhao import Caminhao
from moto import Moto


def main():
    v1 = Moto(20)
    v1.calc_frete()

    v2 = Drone(8)
    v2.calc_frete()

    v3 = Caminhao(80)
    v3.calc_frete()


if __name__ == '__main__':
    main()
