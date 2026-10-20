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

    while hp:

        print(f"Filha de prioridade: {hp}")

        custo_acumulado, tmp = heapq.heappop(hp)

        # se a última letra do caminho (nó atual) for o destino - encontramos um caminho
        if tmp[-1] == destino:
            print(f"{destino} encontrado! - custo total: {custo_acumulado} - caminho: {tmp}")

            resultados.append((custo_acumulado, tmp))
            encontrado = True

        # buscamos as ligações do nó atual
        ligacoes = grafo[tmp[-1]]

        # joga no heap as ligações do nó atual com os caminhos + custo
        for i in range (len(ligacoes)):
            heapq.heappush(hp, (custo_acumulado + ligacoes[i][1], f'{tmp}{ligacoes[i][0]}'))

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