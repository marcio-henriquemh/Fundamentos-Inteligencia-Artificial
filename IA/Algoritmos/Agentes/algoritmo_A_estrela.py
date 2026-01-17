import heapq

def algoritmo_estrela(grafo, no_inicial, heuristica, no_objetivo):
    # Fila de prioridade
    no_abertos = []
    heapq.heappush(no_abertos, (0 + heuristica(no_inicial), no_inicial))
    
    # Registro de caminhos
    pais = {no_inicial: None}
    
    # Custo do início até o nó atual: g(n)
    funcao_g = {no_inicial: 0}
    
    while no_abertos:
        # Pega o nó com menor f(n) = g(n) + h(n)
        _, no_atual = heapq.heappop(no_abertos)
        
        # Objetivo alcançado
        if no_atual == no_objetivo:
            caminho = []
            while no_atual:
                caminho.append(no_atual)
                no_atual = pais[no_atual]
            return caminho[::-1] # Retorna caminho invertido
            
        # Explora vizinhos
        for vizinho in grafo.get(no_atual, []):
            # Custo da aresta é assumido como 1 neste exemplo (grafo não ponderado)
            novo_g = funcao_g[no_atual] + 1
            
            if vizinho not in funcao_g or novo_g < funcao_g[vizinho]:
                funcao_g[vizinho] = novo_g
                f_n = novo_g + heuristica(vizinho)
                heapq.heappush(no_abertos, (f_n, vizinho))
                pais[vizinho] = no_atual
                
    return None # Nenhum caminho encontrado

# GRAFO MODELADO
grafo_caminho_sala = {
    'entrada': ['sala101', 'corredorA'],
    'sala101': [],
    'corredorA': ['sala102', 'sala201'],
    'sala102': [],
    'sala201': ['sala202'],
    'sala202': ['saida'],
    'saida': []
}

# Heurística simples
# distância física,  (x1-x2) + (y1-y2)
def heuristica_simples(no):
    distancias = {
        'entrada': 4, 'sala101': 5, 'corredorA': 2,
        'sala102': 3, 'sala201': 1, 'sala202': 1, 'saida': 0
    }
    return distancias.get(no, 99)

# Chamada da função
resultado = algoritmo_estrela(grafo_caminho_sala, 'entrada', heuristica_simples, 'saida')

# Imprime o resultado
if resultado:
    print(f"Caminho encontrado: {' -> '.join(resultado)}")
else:
    print("Nenhum caminho encontrado.")
