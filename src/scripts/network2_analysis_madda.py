# CENTRALITY MEASURES
    # Degree centrality
    # Eigenvector centrality
    # Closeness centrality ( most well connected agents)

    # what are the movies in which our most important (influential and well connected) agents of Network 2 participated and how that is related to the influence ranking of the movie
    # components - clustering coefficient - local clustering coefficient - redundancy (e the connectedness of the network as well as individuate structural holes, hence those nodes, whose missing links give it more control over diffusion of knowledge and information between neighbors)

import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd


with open('./src/graph_files/network2proj.gexf', 'r', encoding='utf-8') as f:
    
# Read the graph from the file
    n2 = nx.read_gexf(f)

# ================ DEGREE CENTRALITY
#I want to find out who are the most connected people in the network
# the function returns a dictionary with nodes as keys and degree as value

degree = nx.degree_centrality(n2)

degree_list = []
for key, value in degree.items():
    tup = (key, value)
    degree_list.append(tup)


highest_degree = degree_list[:20]

names= []
degree= []
role= []
movies= [] #I want to retrieve the movies he collaborated in

for tup in highest_degree:
    r = nx.get_node_attributes(n2, tup[0])
    edges = n2.edges(tup[0], data=True)
    edge_labels = [d['label'] for u, v, d in edges] # u and v are the endpoints of the edge, and d is a dictionary containing any edge attributes.
    names.append(tup[0])
    degree.append(tup[1])
    role.append(r)
    movies.append(edge_labels)


