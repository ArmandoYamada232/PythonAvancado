from rich.traceback import install

install()

'''
Essa biblioteca monitora os erros e demonstra eles com uma visualização melhor

'''


def divisao(x: float, y: float):
    return x / y


def mostrar_divisao():
    print(divisao(10, 0))


mostrar_divisao()
