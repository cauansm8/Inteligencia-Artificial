import heapq

""" 
Busca de custo uniforme (Uniform Cost Search - UCS)

fila de prioridade ordenada por custo -> heap

adequada quando ações possuem custos diferentes

em grafo

g(n) = custo acumulado do início até n

f(n) = g(n)
"""


# feito usando heapq já pronto
def UCS(grafo, raiz, destino): 

    hp = []

    if raiz == destino:
        print(f"{destino} encontrado! - custo total: {0} - caminho: {raiz}")
        return

    heapq.heappush(hp, (0, raiz))

    encontrado = False

    resultados = []

    visitados = set()

    while hp:

        print(f"Filha de prioridade: {hp}")

        custo_acumulado, tmp = heapq.heappop(hp)

        if tmp[-1] in visitados:
            continue

        # Marca o nó atual como visitado
        visitados.add(tmp[-1])

        # se a última letra do caminho (nó atual) for o destino - encontramos um caminho
        if tmp[-1] == destino:
            print(f"{destino} encontrado! - custo total: {custo_acumulado} - caminho: {tmp}")

            resultados.append((custo_acumulado, tmp))
            encontrado = True

        # joga no heap as ligações do nó atual com os caminhos + custo
        for vizinho, custo_aresta in grafo.get(tmp[-1], []):
            if vizinho not in visitados:
                novo_custo = custo_acumulado + custo_aresta
                novo_caminho = f"{tmp}{vizinho}"
                heapq.heappush(hp, (novo_custo, novo_caminho))

    if encontrado == False:
        print("Não encontrado!")
    else:
        resultados.sort()
        print(f"Resultados encontrados: {resultados}")


def main():
    grafo = {
        'S': [('A', 2), ('B', 5)],
        'A': [('C', 2)],
        'B': [('C', 1)],
        'C': [('G', 2)],
        'G': []
    }


    UCS(grafo, 'S', 'G')

main()