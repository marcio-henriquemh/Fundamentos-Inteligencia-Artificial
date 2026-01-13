def busca_profundidade(inicio, objetivo, grafo):
    
    pilha = [inicio]
  
    visitado = set()

  
    while pilha:
        no = pilha.pop() 

        # Se o nó ainda não foi visitado
        if no not in visitado:
            # Marca o nó como visitado
            visitado.add(no)

       
            if no == objetivo:
                return objetivo # Retorna o objetivo (ou a lista de nós visitados/caminho)

            # Adiciona os vizinhos não visitados do nó atual à pilha
            # É necessário ter a estrutura de dados do grafo para acessar os vizinhos
            if no in grafo:
                for vizinho in reversed(grafo[no]): # Inverte para manter a ordem LIFO/FIFO para vizinhos
                    if vizinho not in visitado:
                        pilha.append(vizinho)

    # Se a pilha esvaziar e o objetivo não for encontrado
    return None



# Exemplo de uso
meu_grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

inicio_busca = 'A'
objetivo_busca = 'F'

resultado = busca_profundidade(inicio_busca, objetivo_busca, meu_grafo)
print(f"Objetivo {objetivo_busca} encontrado: {resultado is not None}")
