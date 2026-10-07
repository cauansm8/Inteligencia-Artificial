"""
BFS - Breadth-First Search - Busca em largura

FIFO - first in, first out -> fila

Em árvore
"""

def BFS(raiz, destino):
    f = []

    f.append(raiz)

    v = f.pop(0)
    
    print(f"Analisando: {v.valor}")

    if v.valor == destino:
        print("ENCONTRADO!")
        return

    # add se nn forem nulos
    if v.esq:
        f.append(v.esq)
    if v.dir:        
        f.append(v.dir)

    while f:
        v = f.pop(0)

        print(f"Analisando: {v.valor}")

        if v.valor == destino:
            print("ENCONTRADO!")
            return

        # add se nn forem nulos
        if v.esq:
            f.append(v.esq)
        if v.dir:        
            f.append(v.dir)

    print("NÃO FOI ENCONTRADO!")


# estrutura nó
class No:
    def __init__(self, valor):
        self.valor = valor
        self.esq = None
        self.dir = None


def main():

    """ 
            A
        B       C
    D      E  F   G
     """


    raiz = No('A')
    
    esq1 = No('B')
    dir1 = No('C')

    raiz.esq = esq1
    raiz.dir = dir1


    esq2 = No('D')
    dir2 = No('E')

    esq1.esq = esq2
    esq1.dir = dir2

    esq3 = No('F')
    dir3 = No('G')

    dir1.esq = esq3
    dir1.dir = dir3


    BFS(raiz, 'F')

main()