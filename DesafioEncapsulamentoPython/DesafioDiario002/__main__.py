from DesafioEncapsulamentoPython.DesafioDiario002.diario import Diario
from rich import inspect


def main():
    d = Diario('teste123')
    d.escrever = 'Ola'
    d.escrever = 'Seu cu é peludo'
    d.escrever = 'sua mãe é trans'
    d.ler_diario('teste123')
    # inspect(d, methods=True, private=True)


if __name__ == '__main__':
    main()
