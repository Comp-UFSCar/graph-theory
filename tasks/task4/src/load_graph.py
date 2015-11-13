__author__ = 'Thales Menato'
__author__ = 'Daniel Nobusada'

import numpy as np
import networkx as nx

def load_graph(graph_path, label_path):
    """
        Carrega os arquivos para simulacao na estrutura grafo do NetworkX

    Parametros
    ----------
    graph_path: string
        Path para o arquivo contendo a matriz de adjacencia

    label_path: string
        Path para o arquivo contendo os nomes dos vertices

    Return
    ------
    G
        estrutura grafo da networkx
    """

    adj_matrix = np.loadtxt(graph_path)
    labels = np.loadtxt(label_path, dtype=basestring, delimiter='\n')

    # Obtem as coordenadas em que o peso eh nao-nulo
    rows, cols = np.where(adj_matrix > 0)

    # Obtem o peso de cada uma das arestas
    weight = [adj_matrix[rows[i], cols[i]] for i in range(0, len(rows))]

    # Cria lista de arestas com peso
    edges_with_weight = zip(rows.tolist(), cols.tolist(), weight)

    # Cria um grafo vazio usando NetworkX
    G = nx.Graph()

    # Insere primeiro os vertices nomeados
    set_edges = set(rows.tolist())
    for i in range(0, len(set_edges)):
        G.add_node(i, name=labels.tolist()[i])

    # Insere as arestas
    G.add_weighted_edges_from(edges_with_weight)

    return G

