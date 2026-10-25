import numpy as np
import heapq as hp


"""

g(n) = custo acumulado do início até n
h(n) = custo estimado de n ao objetivo



Busca gulosa = escolhe o nó com menor h(n) - considera apenas a estimativa restante
Busca A* = escolhe o nó com menor f(n) - considera o custo acumulado e a estimativa

f(n) = g(n) + h(n) = custo total estimado passando por n
(se h(n) = 0, vira o UCS)

h(n) = função heurística (manhattan, euclidiana)
"""



def busca_A_estrela(origem, destino, grafo, posicoes):

    f = []

    x0, y0 = posicoes[origem]
    x1, y1 = posicoes[destino]

    # parâmetros:
    # f(n) = h(n) + g(n)
    # origem -> estado atual
    # esse [origem] guarda o caminho
    # g(n) -> acumulado
    # o heap ordena com base no menor f(n)
    hp.heappush(f, (funcao_heuristica(x0, y0, x1, y1) + 0, origem, [origem], 0))

    # controle dos nós visitados (não terá problema, pois é unidirecional, mas é uma boa prática)
    visitados = set()

    while f:

        acumulado_com_heuristica, atual, caminho, acumulado_real = hp.heappop(f)

        if atual in visitados:
            continue

        if atual != destino:
            visitados.add(atual)

        print(f"Visitando: {atual[0]}")

        if atual[0] == destino:
            print(f"O {destino} foi encontrado: caminho {caminho} - custo: {acumulado_real}")
            

        x0, y0 = posicoes[destino]

        for vizinho, peso in grafo[atual[0]]:

            if vizinho not in visitados:
                x1, y1 = posicoes[vizinho[0]]

                h = funcao_heuristica (x0, y0, x1, y1)
                g = peso + acumulado_real

                # o primeiro termo é o f(n) = g(n) + h(n) -> ele é quem decide qual caminho vai ser tomado (o menor)
                hp.heappush(f, (h + g, vizinho, caminho + [vizinho], g))



# função heurística -> distância entre pontos
def funcao_heuristica(x0, y0, x1, y1):
    return (np.sqrt ((x1 - x0)** 2 + (y1- y0)**2))


def main ():
    grafo = {
    'A' : {('B', np.random.randint(1, 5)), ('C', np.random.randint(1, 5))},
    'B' : {('D', np.random.randint(1, 5)), ('E', np.random.randint(1, 5))},
    'C' : {('F', np.random.randint(1, 5))},
    'D' : {('G', np.random.randint(1, 5))},
    'E' : {('G', np.random.randint(1, 5))},
    'F' : {('H', np.random.randint(1, 5)), ('G', np.random.randint(1, 5))},
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

    print(grafo)    
    print(posicao)


    busca_A_estrela('A', 'G', grafo, posicao)



main()








