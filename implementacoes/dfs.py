import networkx as nx

def dfs(grafo, alvo):
    lista = list(grafo.neighbors(1))
    lista.reverse()

    while(lista != []):
        no = lista.pop()
        print(no, 'visitado')
        if(no == alvo):
            print('Encontrado: ', alvo)
            break

        vizinhos = list(grafo.neighbors(no))
        vizinhos.reverse()
        for vizinho in vizinhos:
            lista.append(vizinho)



g = nx.DiGraph()

vertices = [1,2,3,4,5,6,7,8,9,10]
arestas = [(1,2),(1,3),(1,4),(2,5),(3,7),(3,8),(4,9),(5,6),(9,10)]

g.add_nodes_from(vertices)
g.add_edges_from(arestas)

dfs(g,10)



