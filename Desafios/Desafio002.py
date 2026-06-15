from rich import print
from rich.panel import Panel

class Produto:
    def __init__(self, nome: str, preco: float):
        self.nome = nome
        self.preco = preco

    def etiqueta_produto(self):
        etiqueta = Panel(f'Produto: {self.nome} \n{10*'-='}\nPreço: R${self.preco} reais',title='PRODUTO', width= 40)
        return etiqueta

produto1 = Produto('Mouse', 100)
print(produto1.etiqueta_produto())