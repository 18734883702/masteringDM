# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 10:57:38 2016

@author: megan squire
"""

import networkx as nx

g = nx.read_weighted_edgelist('data/edgelist64.csv')


graphs = list(nx.connected_component_subgraphs(g))
cc = graphs[0]

ego = nx.Graph(nx.ego_graph(cc, 'tirsen', radius=3))

graphDegree = nx.degree(ego)

pos=nx.spring_layout(ego)

nx.draw(ego,
        pos,
        node_size=[v * 10 for v in graphDegree.values()],
        with_labels=True,
        font_size=8)
      
nx.draw_networkx_nodes(ego,
                       pos,
                       nodelist=['tirsen'],
                       node_size=300,
                       node_color='g')
