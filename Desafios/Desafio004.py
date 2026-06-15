from rich import print


class Livro:
    def __init__(self, titulo, total_de_paginas):
        self.titulo = titulo
        self.total_de_paginas = total_de_paginas
        self.pagina_atual = 1

        print(
            f'Você acabou de abrir o livro com titulo: {self.titulo} que tem {self.total_de_paginas} páginas e você está na página {self.pagina_atual}')

    def avancar_paginas(self, qtd_paginas = 1):
        cont = 0
        for pagina in range(0, qtd_paginas, 1):
            if not self.fim_do_livro():
                self.pagina_atual +=1
                print(f'Você avançou para página {self.pagina_atual} páginas ->', end=' ')
                cont += 1
        print(f'Você está na pág {self.pagina_atual}')

    def fim_do_livro(self) -> bool:
        if self.pagina_atual == self.total_de_paginas:
            return True
        else:
            return False

livro1 = Livro('Livro 1', 100)

livro1.avancar_paginas(4)
