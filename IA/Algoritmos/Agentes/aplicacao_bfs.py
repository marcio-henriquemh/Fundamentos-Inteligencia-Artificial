def busca_em_largura(grafo, inicio, objetivo):
    # A fila armazena os caminhos, começando com o caminho [inicio]
    fila = [[inicio]]
    # O conjunto visitados armazena apenas os nós que já foram visitados para evitar loops
    visitados = set()
    visitados.add(inicio)

    while fila:
        # Pega o primeiro caminho da fila
        caminho = fila.pop(0)
        # Pega o último nó do caminho (o nó atual)
        no_atual = caminho[-1]

        # Se o nó atual for o objetivo, retornamos o caminho completo
        if no_atual == objetivo:
            return caminho

        # Itera sobre os vizinhos do nó atual
        if no_atual in grafo:
            for vizinho in grafo[no_atual]:
                if vizinho not in visitados:
                    # Cria um novo caminho estendendo o caminho atual com o vizinho
                    novo_caminho = list(caminho)
                    novo_caminho.append(vizinho)
                    # Adiciona o novo caminho à fila
                    fila.append(novo_caminho)
                    # Marca o vizinho como visitado
                    visitados.add(vizinho)

    # Se a fila esvaziar e o objetivo não for encontrado, retorna None
    return None

# GRAFO MODELADO (chave 'corredoA' corrigida para 'corredorA')
grafo_caminho_sala = {
    'entrada': ['sala101', 'corredorA'],
    'sala101': [],
    'corredorA': ['sala102', 'sala201'],
    'sala102': [],
    'sala201': ['sala202'],
    'sala202': ['saida'],
    'saida': []
}

# Chamada da função com todos os argumentos necessários
resultado = busca_em_largura(grafo_caminho_sala, 'entrada', 'saida')

# Imprime o resultado
if resultado:
    print(f"Caminho encontrado: {resultado}")
else:
    print("Nenhum caminho encontrado.")

