from queue import PriorityQueue

def best_first_search(root):
    open = PriorityQueue()
    close = []

    open.put((heuristic(root),root))
    ultimo = []

    while not open.empty():
        v_heuristica,next_state = open.get()
        print(next_state)
        aux = ultimo
        ultimo = next_state
        
        if v_heuristica == 0:
            break


        nos_viznhos = vizinhos(next_state)

        for no in nos_viznhos:
            if no not in close:
                open.put((heuristic(no),no))
        

        close.append(next_state)

        # print(ultimo)

        


    return ultimo


def vizinhos(state):
    lista = []
    linha = 0
    coluna = 0

    for i in range(len(state)):
        for j in range(len(state[0])):
            if state[i][j] == 0:
                linha = i
                coluna = j

    for i in range(2): # nó coluna alterada
        no = [row[:] for row in state]
        # no = list(state)
        vizinho_coluna = (-1)**i + coluna
        if(posicao_valida(vizinho_coluna)):
            aux = no[linha][coluna]
            no[linha][coluna] = no[linha][vizinho_coluna]
            no[linha][vizinho_coluna] = aux
            lista.append(no)

    for i in range(2): # nó linha alterada
        # no = list(state)
        no = [row[:] for row in state]
        vizinho_linha = (-1)**i + linha
        if(posicao_valida(vizinho_linha)):
            aux = no[linha][coluna]
            no[linha][coluna] = state[vizinho_linha][coluna]
            no[vizinho_linha][coluna] = aux
            lista.append(no)

    return lista

    



def posicao_valida(pos):
    if (pos >= 3 or pos < 0):
        return False
    return True



def heuristic(state):
    matriz = [[1,2,3],[4,5,6],[7,8,0]]
    diferenca = 0

    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            diferenca += abs(matriz[i][j] - state[i][j])

    return diferenca


matriz = [[2,1,4],[7,5,6],[3,8,0]]
matriz = [[1,2,3],[4,5,6],[7,0,8]]

solucao = best_first_search(matriz)
print(solucao)


