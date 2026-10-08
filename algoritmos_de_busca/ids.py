"""

Busca de aprofundamento iterativo (Iterative Deepening Search - IDS)

- completeza da BFS
- uso de memória da DFS
- pilha


"""

def buscar(raiz, destino, limite):
    p = []

    p.insert(0, (raiz, 0))

    while p:
        tmp, n = p.pop(0)

        if n <= limite:

            print(f"Visitando {tmp.valor}")

            if tmp.valor == destino:
                return True

            if tmp.dir:
                p.insert(0, (tmp.dir, n+1))
            if tmp.esq:
                p.insert(0, (tmp.esq, n+1))

    return False

# descobrir o maior nivel -> limite max
def descobrir_nivel_max(raiz):
    p = []

    p.insert(0, (raiz, 0))

    nivel_max = 0

    while p:
        tmp, n = p.pop(0)

        if (n > nivel_max):
            nivel_max = n

        if tmp.esq:
            p.insert(0, (tmp.esq, n+1))
        if tmp.dir:
            p.insert(0, (tmp.dir, n+1))

    return nivel_max


def IDS (raiz, destino):
    limite_max = descobrir_nivel_max(raiz)

    for i in range (0, limite_max + 1):
        ret = buscar(raiz, destino, i)

        if ret:
            print(f"Encontrado com limite {i} -> destino: {destino}")
            break
        else:
            print(f"Não encontrado com limite {i}")


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


    IDS(raiz, 'F')

main()
