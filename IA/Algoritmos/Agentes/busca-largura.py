def busca_largura(inicio, objetivo, grafo):
    fila = [inicio]
    conj_visitado = set()
    
    # Adiciona o nó inicial ao conjunto de visitados imediatamente
    conj_visitado.add(inicio) 
    
    while fila:
        # Remover o primeiro elemento da fila (operação FIFO)
        no = fila.pop(0) 

        # Verificar se o nó atual é o objetivo
        if no == objetivo:
            return no
        
        # Iterar sobre os vizinhos do nó atual, se existirem
        if no in grafo:
            for vizinho in grafo[no]: # A ordem (reversed ou não) depende da preferência, mas 'reversed' não é necessário para a BFS padrão
                if vizinho not in conj_visitado:
                    # Adicionar o vizinho à fila e ao conjunto de visitados
                    fila.append(vizinho)
                    conj_visitado.add(vizinho)
    
    # Se o loop terminar e o objetivo não for encontrado, retorne None (ou mensagem de erro)
    return None
