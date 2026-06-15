from guerreiro import Guerreiro
from mago import Mago


def main():
    personagem1 = Guerreiro('Kratos', 5000)
    #personagem1.mostrar_personagem()
    personagem2 = Mago('Harry Potter', 2500)
    #personagem2.mostrar_personagem()

    personagem2.atacar(personagem1, 200)
    personagem1.curar()

    personagem1.atacar(personagem2,300)


if __name__ == '__main__':
    main()
