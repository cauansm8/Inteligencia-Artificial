import numpy as np
import heapq as hp

"""

g(n) = custo acumulado do início até n
h(n) = custo estimado de n ao objetivo


Busca gulosa = escolhe o nó com menor h(n) - considera apenas a estimativa restante
Busca A* = escolhe o nó com menor f(n) - considera o custo acumulado e a estimativa

f(n) = h(n)
h(n) = função heurística (manhattan, euclidiana)
"""


def busca_gulosa(origem, destino, grafo, posicoes):

    f = []
    hp.heappush(f, (0, origem, [origem]))

    # controle dos nós visitados (não terá problema, pois é unidirecional, mas é uma boa prática)
    visitados = set()

    while f:

        heuristica, atual, caminho = hp.heappop(f)

        if atual in visitados:
            continue

        visitados.add(atual)

        print(f"Visitando: {atual}")

        if atual == destino:
            print(f"O {destino} foi encontrado: caminho {caminho}")
            return caminho

        x0, y0 = posicoes[destino]

        for vizinho in grafo[atual]:

            if vizinho not in visitados:
                x1, y1 = posicoes[vizinho]

                valor_estimado = funcao_heuristica (x0, y0, x1, y1)

                hp.heappush(f, (valor_estimado, vizinho, caminho + [vizinho]))

    print("Destino não encontrado.")
    return None


# função heurística -> distância entre pontos
def funcao_heuristica(x0, y0, x1, y1):
    return int(np.sqrt ((x1 - x0)** 2 + (y1- y0)**2))


def main ():
    grafo = {
    'A' : {'B', 'C'},
    'B' : {'D', 'E'},
    'C' : {'F'},
    'D' : {'G'},
    'E' : {'G'},
    'F' : {'H', 'G'},
    'H' : {},
    'G' : {}
    }

    v_inicial = 1
    v_final = 5

    # posição (coordenadas cartesianas - aleátorias somente para conseguir ver como funciona)
    posicao = {
        'A' : (np.random.randint(v_inicial, v_final), np.random.randint(v_inicial, v_final)),
        'B' : (np.random.randint(v_inicial, v_final), np.random.randint(v_inicial, v_final)),
        'C' : (np.random.randint(v_inicial, v_final), np.random.randint(v_inicial, v_final)),
        'D' : (np.random.randint(v_inicial, v_final), np.random.randint(v_inicial, v_final)),
        'E' : (np.random.randint(v_inicial, v_final), np.random.randint(v_inicial, v_final)),
        'F' : (np.random.randint(v_inicial, v_final), np.random.randint(v_inicial, v_final)),
        'H' : (np.random.randint(v_inicial, v_final), np.random.randint(v_inicial, v_final)),
        'G' : (np.random.randint(v_inicial, v_final), np.random.randint(v_inicial, v_final))
    }
    
    print(posicao)

    busca_gulosa('A', 'G', grafo, posicao)



main()








