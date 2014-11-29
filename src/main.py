__author__ = 'Thales Menato'

import networkx
from plot_graph import plot_graph, plot_hist
import datetime
import numpy as np

def main():
    nodes = [5, 20, 50, 100, 200]
    p_list = [ i / 10.0 for i in range(0, 11)]

    for n in nodes:
        pos = None
        for p in p_list:

            # Grafo R gerado com n vertices e probabilidade p
            R = networkx.erdos_renyi_graph(n, p)

            # Lista com o grau de cada vertice
            degree_list = [R.degree(i) for i in R.nodes()]
            plot_hist(np.asarray(degree_list),
                      title="vertices = " + str(n) + ", p = " + str(p),
                      img_name="[hist]"+str(n)+"_vertices_p_"+str(p),
                      folder=str(n))

            # Escrever os resultados
            # N = 5
            if n is nodes[0]:
                inicio = datetime.datetime.now()

                # Imagens da plotagem do grafo
                if pos is None:
                    pos = plot_graph(R,
                                     iterations=1,
                                     title="vertices = " + str(n) + ", p = " + str(p),
                                     save_figure=True,
                                     img_name=str(n)+"_vertices_p_" + str(p),
                                     folder=str(n))
                else:
                    plot_graph(R,
                               pos=pos,
                               iterations=1,
                               title="vertices = " + str(n) + ", p = " + str(p),
                               save_figure=True,
                               img_name=str(n)+"_vertices_p_" + str(p),
                               folder=str(n))

                print "n = "+str(nodes[0])+"\tp = "+str(p)+"\t\t"+str(datetime.datetime.now()-inicio)

            # N = 20
            elif n is nodes[1]:
                inicio = datetime.datetime.now()

                # Imagens da plotagem do grafo
                if pos is None:
                    pos = plot_graph(R,
                                     iterations=1,
                                     title="vertices = " + str(n) + ", p = " + str(p),
                                     save_figure=True,
                                     img_name=str(n)+"_vertices_p_" + str(p),
                                     folder=str(n))
                else:
                    plot_graph(R,
                               pos=pos,
                               iterations=1,
                               title="vertices = " + str(n) + ", p = " + str(p),
                               save_figure=True,
                               img_name=str(n)+"_vertices_p_" + str(p),
                               folder=str(n))

                print "n = "+str(nodes[1])+"\tp = "+str(p)+"\t\t"+str(datetime.datetime.now()-inicio)

            # N = 50
            elif n is nodes[2]:
                inicio = datetime.datetime.now()

                # Imagens da plotagem do grafo
                if pos is None:
                    pos = plot_graph(R,
                                     iterations=1,
                                     width=0.35,
                                     title="vertices = " + str(n) + ", p = " + str(p),
                                     save_figure=True,
                                     img_name=str(n)+"_vertices_p_" + str(p),
                                     folder=str(n))
                else:
                    plot_graph(R,
                               pos=pos,
                               iterations=1,
                               width=0.35,
                               title="vertices = " + str(n) + ", p = " + str(p),
                               save_figure=True,
                               img_name=str(n)+"_vertices_p_" + str(p),
                               folder=str(n))

                print "n = "+str(nodes[2])+"\tp = "+str(p)+"\t\t"+str(datetime.datetime.now()-inicio)

            # N = 100
            elif n is nodes[3]:
                inicio = datetime.datetime.now()

                # Imagens da plotagem do grafo
                if pos is None:
                    pos = plot_graph(R,
                                     iterations=1,
                                     node_size=400,
                                     width=0.15,
                                     title="vertices = " + str(n) + ", p = " + str(p),
                                     save_figure=True,
                                     img_name=str(n)+"_vertices_p_" + str(p),
                                     folder=str(n))
                else:
                    plot_graph(R,
                               pos=pos,
                               iterations=1,
                               node_size=400,
                               width=0.15,
                               title="vertices = " + str(n) + ", p = " + str(p),
                               save_figure=True,
                               img_name=str(n)+"_vertices_p_" + str(p),
                               folder=str(n))

                print "n = "+str(nodes[3])+"\tp = "+str(p)+"\t\t"+str(datetime.datetime.now()-inicio)

            # N = 200
            elif n is nodes[4]:
                inicio = datetime.datetime.now()

                if pos is None:
                    pos = plot_graph(R,
                                     iterations=1,
                                     node_size=250,
                                     font_size=7,
                                     width=0.05,
                                     title="vertices = " + str(n) + ", p = " + str(p),
                                     save_figure=True,
                                     img_name=str(n)+"_vertices_p_" + str(p),
                                     folder=str(n))
                else:
                    plot_graph(R,
                               pos=pos,
                               iterations=1,
                               node_size=250,
                               font_size=7,
                               width=0.05,
                               title="vertices = " + str(n) + ", p = " + str(p),
                               save_figure=True,
                               img_name=str(n)+"_vertices_p_" + str(p),
                               folder=str(n))

                print "n = "+str(nodes[4])+"\tp = "+str(p)+"\t\t"+str(datetime.datetime.now()-inicio)
            del degree_list
        del pos

if __name__ == '__main__':
    main()
