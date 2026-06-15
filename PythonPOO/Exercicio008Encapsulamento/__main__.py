from exercicio import Conta_Bancaria

def main():
    c1 = Conta_Bancaria('1111', 'Maria', 5000)
    c1.depositar(500)

    print(c1)



if __name__ == '__main__':
    main()