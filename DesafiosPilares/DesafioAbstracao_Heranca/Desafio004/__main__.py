from DesafiosPilares.DesafioAbstracao_Heranca.Desafio004.horista import Horista
from DesafiosPilares.DesafioAbstracao_Heranca.Desafio004.mensalista import Mensalista


def main():
    f1 = Mensalista('Armando', 8900)
    f1.calc_salario()
    f1.analisar_salario()

    f2 = Horista('Dublack', 12, 200)
    f2.calc_salario()
    f2.analisar_salario()



if __name__ == '__main__':
    main()
