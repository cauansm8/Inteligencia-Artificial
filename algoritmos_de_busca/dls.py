"""
DLS - Depth-Limited Search - Busca em profundidade limitada

LIFO - last in, first out -> pilha

Em árvore

evita a exploração infinita em profundidade

"""


# a 
def DLS(raiz, destino, limite):
    
    print(f"Limite: {limite}")
    
    f = []

    f.insert(0, (raiz, 0))

    v, n = f.pop(0)
    
    print(f"Analisando: {v.valor}")

    if v.valor == destino:
        print("ENCONTRADO!")
        return

    # add se nn forem nulos - add o nó e o nível
    if v.esq:
        f.insert(0, (v.esq, 1))
    if v.dir:        
        f.insert(0, (v.dir, 1))

    while f:

        v, n = f.pop(0)

        if n <= limite:

            print(f"Analisando: {v.valor}")

            if v.valor == destino:
                print("ENCONTRADO!")
                return

            # add se nn forem nulos
            if v.esq:
                f.insert(0, (v.esq, n + 1))
            if v.dir:        
                f.insert(0, (v.dir, n + 1))

        else:
            print(f"Nó {v.valor} fora do nivel, indo para outro nó")

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

    limite = 1

    DLS(raiz, 'F', limite)

main()