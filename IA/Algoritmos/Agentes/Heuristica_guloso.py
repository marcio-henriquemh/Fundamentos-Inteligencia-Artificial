import math

class Grafo:
    def __init__(self, vertices, arestas):
        self.V = set(vertices)  # conjunto de vértices
        self.E = set(arestas)   # conjunto de arestas
    
    def __repr__(self):
        return f'Grafo(V={self.V}, E={self.E})'
    
    def adicionar_vertice(self, v):
        self.V.add(v)
    
    def adicionar_aresta(self, u, v):
        self.E.add((u, v))
    
    def obter_vizinhos(self, v):
        """Retorna todos os vizinhos de um vértice"""
        vizinhos = set()
        for aresta in self.E:
            if aresta[0] == v:
                vizinhos.add(aresta[1])
            elif aresta[1] == v:
                vizinhos.add(aresta[0])
        return vizinhos

def produto_cartesiano(G, H):
    """Produto cartesiano de dois grafos G □ H"""
    vertices = [(g, h) for g in G.V for h in H.V]
    
    arestas = set()
    
    # Arestas quando primeiro vértice é igual
    for g in G.V:
        for h1 in H.V:
            for h2 in H.V:
                if (h1, h2) in H.E or (h2, h1) in H.E:
                    arestas.add(((g, h1), (g, h2)))
    
    # Arestas quando segundo vértice é igual
    for h in H.V:
        for g1 in G.V:
            for g2 in G.V:
                if (g1, g2) in G.E or (g2, g1) in G.E:
                    arestas.add(((g1, h), (g2, h)))
    
    return Grafo(vertices, arestas)

class VerticeComCoordenadas:
    """Classe para vértices com coordenadas para cálculo de distância euclidiana"""
    def __init__(self, nome, x, y):
        self.nome = nome
        self.x = x
        self.y = y
    
    def __repr__(self):
        return self.nome
    
    def __hash__(self):
        return hash(self.nome)
    
    def __eq__(self, other):
        return isinstance(other, VerticeComCoordenadas) and self.nome == other.nome

def distancia_euclidiana(v1, v2):
    """Calcula a distância euclidiana entre dois vértices"""
    return math.sqrt((v1.x - v2.x)**2 + (v1.y - v2.y)**2)

def criar_k4_com_coordenadas():
    """Cria um grafo K4 completo com coordenadas para os vértices"""
    # Definindo vértices com coordenadas
    A = VerticeComCoordenadas('A', 0, 0)
    B = VerticeComCoordenadas('B', 2, 2)
    C = VerticeComCoordenadas('C', 2, 0)
    D = VerticeComCoordenadas('D', 0, 2)
    
    vertices = {A, B, C, D}
    
    # Criando todas as arestas possíveis (K4 é completo)
    arestas = set()
    lista_vertices = list(vertices)
    
    for i in range(len(lista_vertices)):
        for j in range(i + 1, len(lista_vertices)):
            arestas.add((lista_vertices[i], lista_vertices[j]))
    
    return Grafo(vertices, arestas)

def busca_gulosa_caminho(grafo, inicio, objetivo, heuristica=distancia_euclidiana):
    """
    Busca gulosa usando heurística de distância euclidiana
    Encontra um caminho do vértice inicial ao objetivo
    """
    caminho = [inicio]
    atual = inicio
    visitados = {inicio}
    
    print(f"Iniciando busca gulosa de {inicio} para {objetivo}")
    print(f"Distância inicial: {heuristica(inicio, objetivo):.2f}")
    
    while atual != objetivo:
        vizinhos = grafo.obter_vizinhos(atual)
        vizinhos_nao_visitados = [v for v in vizinhos if v not in visitados]
        
        if not vizinhos_nao_visitados:
            print("Sem caminho possível - chegou a um beco")
            return None
        
        # Escolhe o vizinho com menor distância euclidiana até o objetivo
        melhor_vizinho = min(vizinhos_nao_visitados, 
                           key=lambda v: heuristica(v, objetivo))
        
        distancia_atual = heuristica(atual, objetivo)
        distancia_melhor = heuristica(melhor_vizinho, objetivo)
        
        print(f"De {atual} (dist: {distancia_atual:.2f}) -> {melhor_vizinho} (dist: {distancia_melhor:.2f})")
        
        caminho.append(melhor_vizinho)
        visitados.add(melhor_vizinho)
        atual = melhor_vizinho
    
    print(f"Objetivo alcançado! Caminho encontrado com {len(caminho)} vértices")
    return caminho

def busca_gulosa_melhor_caminho(grafo, inicio, objetivo, heuristica=distancia_euclidiana):
    """
    Versão mais sofisticada da busca gulosa que tenta encontrar o melhor caminho
    """
    from collections import deque
    
    fila_prioridade = deque([(inicio, [inicio], 0)])  # (vértice, caminho, custo)
    visitados = {inicio: 0}  # vértice: menor custo encontrado
    
    melhor_caminho = None
    menor_custo = float('inf')
    
    while fila_prioridade:
        atual, caminho, custo = fila_prioridade.popleft()
        
        if atual == objetivo:
            if custo < menor_custo:
                menor_custo = custo
                melhor_caminho = caminho
            continue
        
        vizinhos = grafo.obter_vizinhos(atual)
        
        # Ordena vizinhos pela heurística (distância até objetivo)
        vizinhos_ordenados = sorted(vizinhos, 
                                  key=lambda v: heuristica(v, objetivo))
        
        for vizinho in vizinhos_ordenados:
            novo_custo = custo + 1  # custo uniforme
            # novo_custo = custo + heuristica(atual, vizinho)  # custo pela distância
            
            if vizinho not in visitados or novo_custo < visitados[vizinho]:
                visitados[vizinho] = novo_custo
                fila_prioridade.append((vizinho, caminho + [vizinho], novo_custo))
    
    return melhor_caminho

# Exemplo de uso
if __name__ == "__main__":
    # Criando K4
    k4 = criar_k4_com_coordenadas()
    print("Grafo K4 criado:")
    print(f"Vértices: {k4.V}")
    print(f"Arestas: {k4.E}")
    print()
    
    # Testando busca gulosa
    vertices_list = list(k4.V)
    inicio = vertices_list[0]  # A
    objetivo = vertices_list[3]  # D
    
    print("=== BUSCA GULOSA SIMPLES ===")
    caminho_simples = busca_gulosa_caminho(k4, inicio, objetivo)
    if caminho_simples:
        print(f"Caminho encontrado: {' -> '.join(str(v) for v in caminho_simples)}")
    
    print("\n=== BUSCA GULOSA MELHOR CAMINHO ===")
    caminho_melhor = busca_gulosa_melhor_caminho(k4, inicio, objetivo)
    if caminho_melhor:
        print(f"Melhor caminho encontrado: {' -> '.join(str(v) for v in caminho_melhor)}")
        print(f"Comprimento do caminho: {len(caminho_melhor) - 1} arestas")
    
    # Mostrando distâncias entre todos os pares
    print("\n=== DISTÂNCIAS EUCLIDIANAS ===")
    for i, v1 in enumerate(vertices_list):
        for j, v2 in enumerate(vertices_list):
            if i < j:
                dist = distancia_euclidiana(v1, v2)
                print(f"Distância {v1} -> {v2}: {dist:.2f}")