from queue import PriorityQueue

def best_first_search(root):
    open = PriorityQueue()
    close = []

    open.put((heuristic(root),root))
    ultimo = []

    state = root
    menor_valor = heuristic(state)

    while heuristic(state) != 0:
        close.append(state)
        nos_vizinhos = vizinhos(state)

        no_aux = []

        for vizinho in nos_vizinhos:
            if vizinho not in close:
                no_aux.append(vizinho)

        nos_vizinhos = no_aux

        # aux = [row[:] for row in state]

        menor_valor = 999
        o_brabo = []


        if len(nos_vizinhos) == 0:
            h, candidato = open.get()
            while candidato in close:
                h, candidato = open.get()

            state = candidato
            continue           



        for vizinho in nos_vizinhos:
            open.put((heuristic(vizinho),vizinho))
            if heuristic(vizinho) < menor_valor:
                menor_valor = heuristic(vizinho)
                o_brabo = vizinho
        
        state = o_brabo
    

    return state


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
    global posicoes_corretas
    diferenca = 0

    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            numero = state[i][j]
            i_ideal, j_ideal = posicoes_corretas[numero]
            andadas = abs(i - i_ideal) + abs(j - j_ideal)
            diferenca += andadas

    return diferenca


posicoes_corretas = [(2,2),(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1)]


matriz = [[1,2,3],[7,8,0],[4,5,6]]

solucao = best_first_search(matriz)
print(solucao)


