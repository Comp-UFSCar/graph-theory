#!/usr/bin/python
# -*- coding: utf-8 -*-

# Comandos em python para leitura de um grafo a partir de uma matriz de
# adjacencia gravada em arquivo texto

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import os
import platform

# Resolve o caminho absoluto
abs_path = os.path.abspath("sgb128_dist.txt")
pre_path = abs_path[:-(len("sgb128_dist.txt") + 4)]

# Executa para cada dataset individual
dataset_list = ['uk12', 'wg59', 'sgb128']
for dataset in dataset_list:

    # Verifica o sistema operacional
    if platform.system() == 'Linux':
        dataset_dist = pre_path + 'dataset/' + dataset + '_dist.txt'
        dataset_name = pre_path + 'dataset/' + dataset + '_name.txt'
    elif platform.system() == 'Windows':
        dataset_dist = pre_path + 'dataset\\' + dataset + '_dist.txt'
        dataset_name = pre_path + 'dataset\\' + dataset + '_name.txt'

    a = np.loadtxt(dataset_dist)
    labels = np.loadtxt(dataset_name, dtype=basestring, delimiter='\n')

    # Obtem as coordenadas em que o peso eh nao-nulo
    rows, cols= np.where(a > 0)

    # Obtem o peso de cada uma das arestas
    weight = [a[rows[i],cols[i]] for i in range(0, len(rows))]

    # Cria lista de arestas com e sem peso
    edges_with_weight = zip(rows.tolist(), cols.tolist(), weight)

    # Cria um grafo vazio usando NetworkX
    g = nx.Graph()

    # Insere primeiro os vértices nomeados
    set_edges = set(rows.tolist())
    for i in range(0,len(set_edges)):
        g.add_node(i, name=labels.tolist()[i])

    # Insere arestas
    g.add_weighted_edges_from(edges_with_weight)
    # Linka os nomes com seus respectivos vertices

    # Executa o algoritmo de Prim para extrair a MST do grafo
    edge_list = nx.generate_edgelist(g,data=['weight'])
    mst = nx.kruskal_mst(g)

    # Plota resultados, é necessário que seja salvo na mão.
    # Opção de layout de grafo usado foi o Fruchterman & Reingold

    plt.figure(1, figsize=(15,15))		# Cria figura para desenhar grafo: 15 eh a dimensao da imagem
    #nx.draw_spring(mst, node_size=350, font_size=10, edge_width=1, alpha=0.5, arrows=False, with_labels=True)

    # Coordenadas mantém as coordenadas dos vértices do grafo
    coordinates = nx.spring_layout(mst)
    # Salva a primeira imagem
    nx.draw(mst, coordinates, node_size=350, font_size=10, edge_width=1, alpha=0.5, arrows=False, with_labels=True)
    plt.savefig(dataset+'.png')		# Outros formatos: pdf, svg, ...
    plt.show()

    # Função que ordena inversamente pelo peso, por causa da função lambda utilizada
    edges_by_weight = sorted([(i,j,mst.edge[i][j]['weight']) for i,j in mst.edges()], key=lambda a:a[2], reverse=True)
    name_counter = 0
    # Remoção das arestas com maior peso para a detecção de comunidades
    # Press "e" to exit

    print "'Enter' para remover uma aresta, 'e' para passar para o próximo grafo, ou sair do programa no último grafo"
    while raw_input() != "e":
        print "Removendo a aresta de maior peso!!!!!!!!!!!"

        # Remoção efetiva da aresta que possui o maior peso
        mst.remove_edge(edges_by_weight[0][0], edges_by_weight[0][1])
        edges_by_weight = edges_by_weight[1:]

        # Salvar a imagem sem a aresta de maior peso
        plt.figure(1, figsize=(15,15))
        nx.draw(mst, coordinates, node_size=350, font_size=10, edge_width=1, alpha=0.5, arrows=False, with_labels=True)
        plt.savefig(dataset + '_img' + str(name_counter) + '.png')		# Outros formatos: pdf, svg, ...
        plt.show()
        name_counter += 1