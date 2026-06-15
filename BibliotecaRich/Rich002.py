from rich import print
from rich.panel import Panel

caixa = Panel('Olá mundo!', title = 'Mensagem', style = 'red', width = 35)
print(caixa)