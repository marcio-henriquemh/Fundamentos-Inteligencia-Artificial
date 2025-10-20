

import heapq

grafos = {
    'A': {'A': 0, 'B': 3, 'D': 3, 'C': 2},
    'B': {'C': 2, 'D': 3, 'A': 3, 'E': 2},
    'C': {},
    'D': {},
    'E': {}
}


def menor_custo_caminho(grafo,inicio,objetivo):

    fila = [(0, [inicio])]  # (custo_acumulado, caminho)
    visitados = set()

    while fila:
        custo, caminho = heapq.heappop(fila)
        no_atual = caminho[-1]

        print(f"Expandindo {no_atual} com custo {custo}")

        if no_atual == objetivo:
            print("\n Caminho encontrado!")
            print(" → ".join(caminho))
            print(f"Custo total: {custo}")
            return caminho, custo

        if no_atual in visitados:
            continue
        visitados.add(no_atual)

        for vizinho, custo_aresta in grafo.get(no_atual, {}).items():
            if vizinho not in visitados:
                novo_caminho = caminho + [vizinho]
                novo_custo = custo + custo_aresta
                heapq.heappush(fila, (novo_custo, novo_caminho))
                print(f"  Adicionando {vizinho} com custo total {novo_custo}")

    print("Nenhum caminho encontrado.")
    return None, float('inf')

menor_custo_caminho(grafos, 'A', 'E')