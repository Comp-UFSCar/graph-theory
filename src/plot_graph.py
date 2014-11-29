__author__ = 'Thales Menato'

import networkx as nx
import matplotlib.pyplot as plt
import os
import numpy as np

def plot_graph(G,
               iterations=100,
               node_size=1000,
               node_color=(0.8, 0.6, 1),
               font_size=9,
               width=0.5,
               img_name="default",
               title=None,
               pos = None,
               figsize=(16,10),
               k=1,
               save_figure = False,
               folder = None):

    plt.figure(figsize=figsize)
    plt.title(title)
    plt.margins(0)
    plt.axis('off')

    if pos is None:
        pos = nx.spring_layout(G, k=k, iterations=iterations)

    nx.draw_networkx_nodes(G, pos, node_size=node_size, node_color=node_color)
    nx.draw_networkx_edges(G, pos, width=width)

    nx.draw_networkx_labels(G, pos, font_size = font_size)

    if save_figure is True:
        try:
            if folder is not None:
                if not os.path.exists('../generated-data/'+folder):
                    os.makedirs('../generated-data/'+folder)
                plt.savefig('../generated-data/'+folder+'/'+img_name+".jpg", bbox_inches = 'tight', pad_inches=0.2)
            else:
                plt.savefig('../generated-data/'+img_name+".jpg", bbox_inches = 'tight', pad_inches=0.2)
        except IOError:
            print "Erro escrita arquivo"
    else:
        plt.show()
    plt.close()

    return pos

def plot_hist(degree_list, title="", folder=None, img_name="default"):
    plt.figure(0)
    plt.hist(degree_list)
    plt.title(title)
    plt.xlabel("Grau")
    plt.ylabel("Frequencia")
    try:
        if folder is not None:
            if not os.path.exists('../generated-data/'+folder):
                os.makedirs('../generated-data/'+folder)
            plt.savefig('../generated-data/'+folder+'/'+img_name+".jpg", bbox_inches = 'tight', pad_inches=0.2)
        else:
            plt.savefig('../generated-data/'+img_name+".jpg", bbox_inches = 'tight', pad_inches=0.2)
    except IOError:
        print "Erro escrita arquivo"

    plt.close()
