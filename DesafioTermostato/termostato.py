class Termostato:
    def __init__(self):
        self.__temperatura = 24

    @property
    def formated_temperatura(self):
        ftemperatura = self.__temperatura
        return f'{ftemperatura}°C'

    @property
    def temperatura(self):
        return self.__temperatura

    @temperatura.setter
    def temperatura(self, temp):
        if not 16 <= temp <= 30:  # se não estiver (if not) entre 16 e 30
            raise ValueError('A temperatura deve estar entre 16 e 30')
        if (temp % 1 == 0.5) or (temp % 1 == 0):
            print()
        else:
            raise ValueError('Não pode essa temp')
        self.__temperatura = temp
