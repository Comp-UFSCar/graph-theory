__author__ = 'Thales Menato'
__author__ = 'Daniel Nobusada'

import networkx as nx
import matplotlib.pyplot as plt
import datetime

def plot_weighted_graph(G,
                        pos=None,
                        pi=None,
                        writeNodeLabel = False,
                        writeEdgeLabel = False,
                        iterations=100,
                        node_size=1000,
                        node_color=(0.8, 0.6, 1),
                        font_size=9,
                        width=0.5,
                        img_name="default",
                        title=None,
                        figsize=(16,10),
                        k=1,
                        seeds=None,
                        markerscale = 0.5):
    """ Plota um grafo com pesos

    Parametros
    ----------
    G: grafo

    pos: dictionary (default=None)
        Um dicionario com vertices como chaves e posicoes como valores

    pi: dictionary (default=None)
        Um dicionario contendo a lista de predecessores do Dijkstra
        com vertices como chaves e seus predecessores como valores

    writeNodeLabel: bool (default=False)
        Variavel para permitir escrita dos nomes dos vertices

    writeEdgeLabel: bool (default=False)
        Varival para permitir escrita dos pesos nas arestas

    iterations: int (default=100)
        Numero de iteracoes para o spring layout

    node_size: int (default=1000)
        Tamanho dos vertices

    node_color: color string ou array de float (default=(0.8,0.6,1))
        Cor dos vertices na plotagem.
        Obs: eh apenas utilizado caso nao seja passado seeds

    font_size: int (default=9)
        Tamanho da fonte das letras

    width: int (default=0.5)
        Largura das arestas

    img_name: string (default="default")
        Nome do arquivo da imagem gerada

    title: string (default=None)
        Titulo para a plotagem

    figsize: tuple (default=(16,10))
        Dimensoes da figura que sera gerada

    k: float (default=1)
        Distancia otimizada para utilizar no spring_layout

    seeds: list (default=None)
        Lista contendo todos os vertices que foram utilizados como semente

    markerscale: float (default=0.5)
        Float para escala do tamanho que sera utilizado no vertice
        para representacao na legenda

    Returns
    -------
    pos
        dicionario contendo as posicoes dos vertices

    (datetime.datetime.now() - inicio)
        tempo gasto para execucao da plotagem

    nodelist
        lista contendo as listas de vertices conectados por semente
    """
    inicio = datetime.datetime.now()

    colors = {0: (0.1, 0.45, 1),
              1: (0.45, 0.9, 0.45),
              2: (1, 0.9, 0.25),
              3: (1, 0.42, 0.2),
              4: (0.54, 0.18, 0.36)}

    plt.figure(figsize=figsize)
    plt.title(title)
    plt.margins(0)
    plt.axis('off')

    # Se nao foi passado as posicoes dos vertices, calcular elas
    if (pos is None):
        pos = nx.spring_layout(G, k=k, iterations=iterations)

    nodelist = {}
    # Caso o grafo tenha sido obtido a partir do Dijkstra
    if(seeds is not None):
        # Obter a lista de vertices ligados a cada semente utilizada
        Q = G.nodes()
        # Inicializacao sementes em suas nodelist e remocao da lista de vertices
        try:
            for s in seeds:
                    nodelist[s] = [s]
                    del Q[Q.index(s)]
            # Enquanto houver vertices
            while Q:
                temp = []
                u = Q[0]
                del Q[Q.index(u)]

                # Lista de vertices a partir de u ate semente
                while u is not None:
                    temp.append(u)
                    u = pi[u]

                # Para a lista obtida, o ultimo valor eh a semente portanto
                # sera inserido na nodelist[ultimo_valor]
                # todos os vertices obtidos e ja sao removidos de Q (evitar verificacao extra)
                for i in range(0, len(temp) - 1):
                    if temp[i] not in nodelist[temp[len(temp) - 1]]:
                        nodelist[temp[len(temp) - 1]].append(temp[i])
                    if temp[i] in Q:
                        del Q[Q.index(temp[i])]
        except IndexError:
            print "Erro na obtencao do nodelist : imagem " + str(img_name) +\
                   "\nSementes: " + str(seeds) + "\nNodelist: " + str(nodelist)
            exit(-1)
        except ValueError:
            print "Erro na obtencao do nodelist : imagem " + str(img_name) +\
                   "\nSementes: " + str(seeds) + "\nNodelist: " + str(nodelist)
            exit(-1)

        # Lista contendo as sementes ordenadas de acordo com o numero de vertice conectado a elas
        ordem = [i[1] for i in sorted(nodelist.items(), key=lambda x : len(x[1]))]

        # Usando a nodelist obtida, para cada semente (indice),
        # desenhar seus vertices com uma cor pre-definida (colors)
        for i in range(0, len(ordem)):
            nx.draw_networkx_nodes(G, pos,
                                   node_size=node_size,
                                   node_color=colors[i],
                                   nodelist = ordem[i])
        # desenha as arestas
        nx.draw_networkx_edges(G, pos, width=width)

    # Nenhuma semente foi passada, portanto grafo original / completo
    else:
        nx.draw_networkx_nodes(G, pos, node_size=node_size, node_color=node_color)
        nx.draw_networkx_edges(G, pos, width=width)

    # Dicionarios para plotagem dos pesos nas arestas e nomes dos vertices
    weights = { (u, v): info['weight'] for u, v, info in G.edges(data=True) }
    labels = { (u): info['name'] for u, info in G.nodes(data=True) }

    if(writeEdgeLabel is True):
        nx.draw_networkx_edge_labels(
            G, pos, edge_labels=weights, font_size = font_size, font_family='sans-serif')

    if(writeNodeLabel is True):
        nx.draw_networkx_labels(G, pos, labels, font_size = font_size)
    else:
        nx.draw_networkx_labels(G, pos, font_size = font_size)

    if seeds is not None:
        ordem = [i[0] for i in sorted(nodelist.items(), key=lambda x : len(x[1]))]
        # Label para legenda contendo nome do vertice(semente) e numero de vertices conectados a ele
        lbl = [labels[i].split(" ")[0]+" [" + str(len(nodelist[i])) + "]" for i in ordem]

        if writeNodeLabel is False:
            plt.legend(sorted(tuple(seeds)), title="Sementes", scatterpoints = 1, markerscale = markerscale)
        else:
            plt.legend(tuple(lbl), title="Sementes", scatterpoints = 1, markerscale = markerscale,
                       fontsize='small', framealpha=0.5)

    plt.savefig('../generated-data/'+img_name+".png", bbox_inches = 'tight', pad_inches=0.2)
    plt.close()
    return pos, (datetime.datetime.now() - inicio), nodelist


def write_images(data,
                 uk12=True,
                 wg59=True,
                 usair97=True):
    """ Gera as imagens dos dados obtidos na simulacao

    Parametros
    ----------
    data: dictionary
        Dicionario contendo dicionarios com todas as informacoes obtidas
        durante a simulacao nos grafos

    uk12: bool (default=True)
        Define se o grafo uk12 sera plotado

    wg59: bool (default=True)
        Define se o grafo wg59 sera plotado

    usair97: bool (default=True)
        Define se o grafo usair97 sera plotado
    """

    print "Tempo geracao das imagens: "

    # Imagens para o grafo UK12
    if uk12 is True:
        # Grafo original
        pos, tempo, data['uk12']['nodelist'] = \
            plot_weighted_graph(data['uk12']['grafo'],
                                title="Grafo uk12 - Original",
                                img_name="uk12__original",
                                writeEdgeLabel=True,
                                writeNodeLabel=True,
                                node_size=4000,
                                iterations=1,
                                width=2)

        print "Grafo uk12 - Original\t\t" + str(tempo)

        # Simulacao A: sementes espalhadas
        h = data['uk12']['a']['h']
        pi = data['uk12']['a']['pi']
        pos, tempo, data['uk12']['a']['nodelist'] = \
            plot_weighted_graph(h, pos=pos,
                                title="Grafo uk12 - a",
                                img_name="uk12_a",
                                writeEdgeLabel=True,
                                writeNodeLabel=True,
                                seeds=data['uk12']['a']['seeds'],
                                pi=pi,
                                node_size=4000,
                                iterations=1,
                                width=2,
                                markerscale=0.2)

        print "Grafo uk12 - a\t\t\t\t" + str(tempo)

        # Simulacao B: sementes proximas
        h = data['uk12']['b']['h']
        pi = data['uk12']['b']['pi']
        pos, tempo, data['uk12']['b']['nodelist'] = \
            plot_weighted_graph(h, pos=pos,
                                title="Grafo uk12 - b",
                                img_name="uk12_b",
                                writeEdgeLabel=True,
                                writeNodeLabel=True,
                                seeds=data['uk12']['b']['seeds'],
                                pi=pi,
                                node_size=4000,
                                iterations=1,
                                width=2,
                                markerscale=0.2)

        print "Grafo uk12 - b\t\t\t\t" + str(tempo)

    # Imagens para o grafo WG59
    if wg59 is True:
        # Grafo original
        pos, tempo, data['wg59']['nodelist'] = \
            plot_weighted_graph(data['wg59']['grafo'],
                                title="Grafo wg59 - Original",
                                img_name="wg59__original",
                                writeNodeLabel=True,
                                node_size= 1200,
                                iterations=10,
                                width=0.3)

        print "Grafo wg59 - Original\t\t" + str(tempo)

        # Simulacao A: sementes espalhadas
        h = data['wg59']['a']['h']
        pi = data['wg59']['a']['pi']
        pos, tempo, data['wg59']['a']['nodelist'] = \
            plot_weighted_graph(h, pos=pos,
                                title="Grafo wg59 - a",
                                img_name="wg59_a",
                                writeNodeLabel=True,
                                writeEdgeLabel=True,
                                seeds=data['wg59']['a']['seeds'],
                                pi=pi,
                                iterations=10,
                                node_size= 1200,
                                width=0.3,
                                markerscale=0.3)

        print "Grafo wg59 - a\t\t\t\t" + str(tempo)

        # Simulacao B: sementes proximas
        h = data['wg59']['b']['h']
        pi = data['wg59']['b']['pi']
        pos, tempo, data['wg59']['b']['nodelist'] = \
            plot_weighted_graph(h, pos=pos,
                                title="Grafo wg59 - b",
                                img_name="wg59_b",
                                writeEdgeLabel=True,
                                writeNodeLabel=True,
                                seeds=data['wg59']['b']['seeds'],
                                pi=pi,
                                iterations=10,
                                node_size= 1200,
                                width=0.3,
                                markerscale=0.3)

        print "Grafo wg59 - b\t\t\t\t" + str(tempo)

    # Imagens para o grafo USAir97
    if usair97 is True:
        # Grafo original
        pos, tempo, data['usair97']['nodelist']= \
            plot_weighted_graph(data['usair97']['grafo'],
                                title="Grafo USAir97 - Original",
                                img_name="usair97__original",
                                font_size=5,
                                node_size= 200,
                                iterations=1,
                                width=0.1,
                                figsize=(20,10))

        print "Grafo USAir97 - Original\t" + str(tempo)

        # Simulacao A: sementes espalhadas
        h = data['usair97']['a']['h']
        pi = data['usair97']['a']['pi']
        pos, tempo, data['usair97']['a']['nodelist'] = \
            plot_weighted_graph(h, pos=pos,
                                title="Grafo USAir97 - a",
                                img_name="usair97_a",
                                writeEdgeLabel=True,
                                writeNodeLabel=True,
                                seeds=data['usair97']['a']['seeds'],
                                pi=pi,
                                iterations=1,
                                font_size=5,
                                node_size=200,
                                width=0.1,
                                figsize=(20,10))

        print "Grafo USAir97 - a\t\t\t" + str(tempo)

        # Simulacao B: sementes proximas
        h = data['usair97']['b']['h']
        pi = data['usair97']['b']['pi']
        pos, tempo, data['usair97']['b']['nodelist'] = \
            plot_weighted_graph(h, pos=pos,
                                title="Grafo USAir97 - b",
                                img_name="usair97_b",
                                writeEdgeLabel=True,
                                writeNodeLabel=True,
                                seeds=data['usair97']['b']['seeds'],
                                pi=pi,
                                iterations=1,
                                font_size=5,
                                node_size=200,
                                width=0.1,
                                figsize=(20,10))

        print "Grafo USAir97 - b\t\t\t" + str(tempo)