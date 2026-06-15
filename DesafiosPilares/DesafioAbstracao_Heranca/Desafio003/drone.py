from transporte import Transporte


class Drone(Transporte):
    def __init__(self, distancia):
        super().__init__(distancia)

    def calc_frete(self):
        Drone.fator = 9.50
        if self.distancia <= 10:
            frete = self.distancia * Drone.fator
            print(
                f'O frete de {self.__class__.__name__} em distância em {self.distancia} km é igual a R${frete:.2f} reais.\n')
        else:
            print(f'Distancia de: {self.distancia}km só é permitido o transporte por esse veículo de menos de 10 km.\n')
