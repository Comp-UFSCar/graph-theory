__author__ = 'Thales Menato'
__author__ = 'Daniel Nobusada'

from plot_graph import write_images
from load_graph import load_graph
from dijkstra import *
from write_simulation import write_simulation
import networkx as nx
import numpy as np
import datetime

data_path = '../data/'
data = {
    'uk12':{'dist':data_path + 'uk12distB.txt','name':data_path + 'uk12_name.txt'},
    'wg59':{'dist':data_path + 'wg59distB.txt','name':data_path + 'wg59_name.txt'},
    'usair97':{'dist':data_path + 'USAir97.txt','name':data_path + 'USAir_names.txt'}
    }

if __name__ == '__main__':
    """
    Notas:
    1.  Algumas vezes o script esta entrando em loop infinito,
        caso demore mais que 5~10 segundos para haver o primeiro
        output com o tempo de geracao das imagens no console
    2.  Ha um 'bug' que ocorre raramente durante a plotagem onde
        o numero de cores representados eh maior que o numero devido
        aumentando as comunidades distintas encontradas. - erro

    Caso qualquer uma delas aconteca, favor abordar e/ou executar o codigo novamente
    Grato pela compreensao
    """
    inicio = datetime.datetime.now()

    # Grafos onde havera simulacao
    uk12 = True
    wg59 = True
    usair97 = True

    if uk12 is True:
        # Simulacao do grafo UK12, com k = 2
        data['uk12']['a'] = {}
        data['uk12']['b'] = {}
        data['uk12']['lbl'] = []

        data['uk12']['grafo'] = load_graph(data['uk12']['dist'],data['uk12']['name'])

        # Lista com os nomes dos vertices
        for i in data['uk12']['grafo'].nodes(data=True):
            data['uk12']['lbl'].append(i[1]['name'])

        # Usaremos a periferia para obter duas sementes espalhadas
        data['uk12']['a']['seeds'] = nx.periphery(data['uk12']['grafo'])

        # Usaremos um vertice aleatorio e um de seus vizinhos como sementes proximas uma da outra
        random_v = np.random.randint(0, len(data['uk12']['grafo'].nodes()))

        data['uk12']['b']['seeds'] = ([random_v,
                     data['uk12']['grafo'].neighbors(random_v)
                     [np.random.randint(0, len(data['uk12']['grafo'].neighbors(random_v)))]])

        # Executando o Dijkstra nas sementes
        data['uk12']['a']['lambda'], \
        data['uk12']['a']['pi'],\
        data['uk12']['a']['h'] = dijkstra(data['uk12']['grafo'], data['uk12']['a']['seeds'])

        data['uk12']['b']['lambda'], \
        data['uk12']['b']['pi'], \
        data['uk12']['b']['h'] = dijkstra(data['uk12']['grafo'], data['uk12']['b']['seeds'])

    if wg59 is True:
        # Simulacao do grafo WG59, com k = 3
        data['wg59']['a'] = {}
        data['wg59']['b'] = {}
        data['wg59']['lbl'] = []

        data['wg59']['grafo'] = load_graph(data['wg59']['dist'],data['wg59']['name'])
        for i in data['wg59']['grafo'].nodes(data=True):
            data['wg59']['lbl'].append(i[1]['name'])

        # Usaremos a periferia para obter tres sementes espalhadas
        data['wg59']['a']['seeds'] = []

        periferia = nx.periphery(data['wg59']['grafo'])

        for i in range(0, 3):
            random_v = periferia[np.random.randint(0, len(periferia))]
            # Nao permite que a semente original seja uma das ja utilizadas para o a
            while random_v in data['wg59']['a']['seeds']:
                random_v = periferia[np.random.randint(0, len(periferia))]
            data['wg59']['a']['seeds'].append(random_v)

        # Primeira semente inserida na lista
        random_v = np.random.randint(0, len(data['wg59']['grafo'].nodes()))

        vizinhos = data['wg59']['grafo'].neighbors(random_v)
        while len(vizinhos) < 2:
            random_v = np.random.randint(0, len(data['wg59']['grafo'].nodes()))
            vizinhos = data['wg59']['grafo'].neighbors(random_v)

        data['wg59']['b']['seeds'] = [random_v]

        # Proximas duas sementes
        for i in range(0, 2):
            random_v = vizinhos[np.random.randint(0, len(vizinhos))]
            # Enquanto o valor random ja estiver na lista de sementes selecionadas para b
            while random_v in data['wg59']['b']['seeds']:
                random_v = vizinhos[np.random.randint(0, len(vizinhos))]
            # Coloca o valor na lista b
            data['wg59']['b']['seeds'].append(random_v)

        # Executando o Dijkstra nas sementes
        data['wg59']['a']['lambda'], \
        data['wg59']['a']['pi'],\
        data['wg59']['a']['h'] = dijkstra(data['wg59']['grafo'], data['wg59']['a']['seeds'])

        data['wg59']['b']['lambda'], \
        data['wg59']['b']['pi'], \
        data['wg59']['b']['h'] = dijkstra(data['wg59']['grafo'], data['wg59']['b']['seeds'])

    if usair97 is True:
        # Simulacao do grafo USAir97, com k = 5
        data['usair97']['a'] = {}
        data['usair97']['b'] = {}
        data['usair97']['lbl'] = []

        data['usair97']['grafo'] = load_graph(data['usair97']['dist'],data['usair97']['name'])
        for i in data['usair97']['grafo'].nodes(data=True):
            data['usair97']['lbl'].append(i[1]['name'])

        # Usaremos a periferia para obter cinco sementes espalhadas
        data['usair97']['a']['seeds'] = []

        periferia = nx.periphery(data['usair97']['grafo'])

        for i in range(0, 5):
            random_v = periferia[np.random.randint(0, len(periferia))]
            # Nao permite que a semente original seja uma das ja utilizadas para o a
            while random_v in data['usair97']['a']['seeds']:
                random_v = periferia[np.random.randint(0, len(periferia))]
            data['usair97']['a']['seeds'].append(random_v)


        # Primeira semente inserida na lista
        random_v = np.random.randint(0, len(data['usair97']['grafo'].nodes()))

        vizinhos = data['usair97']['grafo'].neighbors(random_v)
        while len(vizinhos) < 2:
            random_v = np.random.randint(0, len(data['usair97']['grafo'].nodes()))
            vizinhos = data['usair97']['grafo'].neighbors(random_v)

        data['usair97']['b']['seeds'] = [random_v]

        # Proximas duas sementes
        for i in range(0, 4):
            vizinhos = data['usair97']['grafo'].neighbors(random_v)
            random_v = vizinhos[np.random.randint(0, len(vizinhos))]
            # Enquanto o valor random ja estiver na lista de sementes selecionadas para b
            while random_v in data['usair97']['b']['seeds']:
                random_v = vizinhos[np.random.randint(0, len(vizinhos))]
            # Coloca o valor na lista b
            data['usair97']['b']['seeds'].append(random_v)

        # Executando o Dijkstra nas sementes
        data['usair97']['a']['lambda'], \
        data['usair97']['a']['pi'],\
        data['usair97']['a']['h'] = dijkstra(data['usair97']['grafo'], data['usair97']['a']['seeds'])

        data['usair97']['b']['lambda'], \
        data['usair97']['b']['pi'], \
        data['usair97']['b']['h'] = dijkstra(data['usair97']['grafo'], data['usair97']['b']['seeds'])
    # Fim das simulacoes

    if uk12 or wg59 or usair97 is True:
        # Escrita dos resultados
        # Gera imagens das comunidades encontradas
        write_images(data, uk12=uk12, wg59=wg59, usair97=usair97)
        # Escreve arquivo txt com dados obtidos da simulacao
        write_simulation(data, uk12=uk12, wg59=wg59, usair97=usair97)

    print "\nTempo total execucao:\t\t" + str(datetime.datetime.now() - inicio)