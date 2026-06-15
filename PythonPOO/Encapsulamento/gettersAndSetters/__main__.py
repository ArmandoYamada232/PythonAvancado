from PythonPOO.Encapsulamento.property.property import Avaliacao


def main():
    av1 = Avaliacao('Dublack', 'Micro computadores e controladores')
    av1.nota = 8

    print(f'O aluno: {av1.nome} tirou {av1.nota} na disciplina: {av1.disciplina}')




if __name__ == '__main__':
    main()