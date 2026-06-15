from rich import print
from rich.table import Table

tabela = Table(title='Tabela de preços')
tabela.add_column('nome', justify='center',style='cyan')
tabela.add_column('preço',justify='center',style='blue')

tabela.add_row('Ovos', 'R$ 25,00')

print(tabela)
