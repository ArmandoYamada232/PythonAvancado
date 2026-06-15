from transporte import Transporte


class Moto(Transporte):
    def __init__(self, distancia):
        super().__init__(distancia)

    def calc_frete(self):
        Moto.fator = 0.50
        frete = Moto.fator * self.distancia
        print(
            f'O frete de {self.__class__.__name__} em distância em {self.distancia} km é igual a R${frete:.2f} reais.\n')
