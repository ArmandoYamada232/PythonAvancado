from DesafiosPilares.DesafioAbstracao_Heranca.Desafio005_remake.guerreiro import Guerreiro



def main():
    per1 = Guerreiro('Goku', 3200)
    per2 = Guerreiro('Vegeta', 3000)

    per1.atacar(per2, 300)
    per2.curar()


if __name__ == '__main__':
    main()