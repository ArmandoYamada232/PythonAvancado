from transporte import Transporte


class Caminhao(Transporte):
    def __init__(self, distancia):
        super().__init__(distancia)

    def calc_frete(self):
        Caminhao.fator = 1.20
        if self.distancia >= 50:
            frete = self.distancia * Caminhao.fator
            print(
                f'O frete de {self.__class__.__name__} em distância em {self.distancia} km é igual a R${frete:.2f} reais.\n')
        else:
            print(f'Distancia de: {self.distancia}km só é permitido o transporte por esse veículo de mais de 50 km.\n')
