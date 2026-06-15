from rich import print
from rich.panel import Panel


class Churras:
    consumo_media = 0.400
    preco_kg_carne = 82.40
    def __init__(self, numeroConvidados,titulo):
        self.numeroConvidados = numeroConvidados
        self.titulo = titulo

    def analisar(self):
        carneTotal = Churras.consumo_media * self.numeroConvidados
        totalcusto = carneTotal * Churras.preco_kg_carne
        precoporpessoa = totalcusto / self.numeroConvidados
        analise = Panel(f'Cada participante comerá {Churras.consumo_media} gramas de carne e cada kg custa R$ {Churras.preco_kg_carne:.2f} reais\nQuantidade recomendados para comprar: {carneTotal}kg de carne para {self.numeroConvidados} convidados\nO custo total de carne: {totalcusto:.2f} reais\nCada pessoa paragará: R${precoporpessoa:.2f} reais',title=self.titulo,style='green')
        return analise
churras = Churras(15, titulo='Churras')
print(churras.analisar())
