from DesafioTermostato.termostato import Termostato
from rich import inspect


def main():
    t = Termostato()
    t.temperatura = 29.5
    inspect(t, methods=True, private=True)


if __name__ == '__main__':
    main()
