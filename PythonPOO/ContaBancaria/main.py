# classe
class ContaBancaria:
    '''
    Classe de conta bancaria que faz deposito e saca
    '''

    # atributos
    def __init__(self, id, nome_titular, saldo_conta=0):
        self.id = id
        self.nome_titular = nome_titular
        self.saldo_conta = saldo_conta
        print(f'Conta bancaria criada com sucesso! saldo atual:{saldo_conta} ')

    def __str__(self):
        return f'O id da conta: {self.id}/ nome do titular: {self.nome_titular}/ Saldo na conta: R${self.saldo_conta:.2f}'


# metodos
    def depositar(self, valor):
            self.saldo_conta = self.saldo_conta + valor
            print(f'Deposito valor R${valor:.2f} realizado com sucesso na conta: {self.id}!')



    def sacar(self,valor):
        if self.saldo_conta > valor:
            self.saldo_conta = self.saldo_conta - valor
            print(f'Saque valor R${valor:.2f} realizado com sucesso na conta: {self.id}!')
        else:
            print('Saldo insuficiente!')



# objetos
c1 = ContaBancaria(111, 'Armando', 3000)
c1.depositar(100)
c1.sacar(990000)
print(c1)
