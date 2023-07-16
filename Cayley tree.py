#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')
import os, sys
import json
import networkx as nx
import matplotlib.pyplot as plt
import random
import pandas as pd
import scipy
import matplotlib.pyplot as plt


#Construct Cayley tree
def cayley_tree(d, k):
    G = nx.Graph()
    G.add_node(0)

    nodes = [0]
    for i in range(d):
        new_nodes = []
        for node in nodes:
            for j in range(k):
                new_node = k * node + j + 1
                G.add_edge(node, new_node)
                new_nodes.append(new_node)
        nodes = new_nodes

    return G


#Call Ceyeley tree function where k is the degree equals 5 and d is the length equal 8
G = cayley_tree(d=6, k=3)


#Color map to give root node different color than others
color_map = []

for node in G:
    if node < 1:
        color_map.append('red')
    else: 
        color_map.append('green')
        

#Visualize Ceyley tree   
plt.figure(figsize=(14,12))
nx.draw_networkx(G, with_labels=False, node_size=40, node_color=color_map, edge_color='#1E5E93', width=2)
plt.show()


# In[ ]:




