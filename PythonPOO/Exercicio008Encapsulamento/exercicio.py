# classe
class Conta_Bancaria:

    # atributos
    def __init__(self, user_id, nome_titular, saldo_conta=0):
        self.user_id = user_id  # público (+)
        self._nome_titular = nome_titular  # protegido (#)
        self.__saldo_conta = saldo_conta  # privado (-)
        print(f'Conta bancaria criada com sucesso! saldo atual:{saldo_conta} ')

    def __str__(self):
        return f'O id da conta: {self.user_id}/ nome do titular: {self._nome_titular}/ Saldo na conta: R${self.__saldo_conta:.2f}'

    # metodos
    def depositar(self, valor):
        valor = abs(valor)
        self.__saldo_conta = self.__saldo_conta + valor
        print(f'Deposito valor R${valor:.2f} realizado com sucesso na conta: {self.user_id}!')


    @property
    def sacar(self, valor):
        valor = abs(valor)
        if self.__saldo_conta > valor:
            self.__saldo_conta = self.__saldo_conta - valor
            print(f'Saque valor R${valor:.2f} realizado com sucesso na conta: {self.user_id}!')
        else:
            print('Saldo insuficiente!')
