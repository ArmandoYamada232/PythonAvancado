from aluno import Aluno


def main():
    a1 = Aluno('Armando', 2002, 00000000, 'engenharia de software')
    print(a1.fazer_aniversario())
    print(a1.apresentar())

if __name__ == '__main__':
    main()
