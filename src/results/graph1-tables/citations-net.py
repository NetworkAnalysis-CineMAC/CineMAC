
import networkx as nx
import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
cwd = os.getcwd()
path= "/".join(list(cwd.split('/')[0:-1])) 

G = nx.read_gexf(path+"/src/graph_files/graph-movie-cit.gexf")

#START MEASURES

#Create a subgraph
import random
import networkx as nx

# Create subgraph

# # Get the nodes in the graph
# nodes = list(G.nodes())
# # Select a random subset of 100 nodes
# random_nodes = random.sample(nodes, 100)
# # Create a subgraph consisting of the selected nodes and their edges
# subgraph = G.subgraph(random_nodes)

# scc_list = list(nx.strongly_connected_components(G))

# create a subgraph consisting of the strongly connected components
# subgraph = nx.DiGraph()
# for scc in scc_list:
#     subgraph.add_edges_from(G.subgraph(scc).edges())


#!Well connected subgraph
degrees = dict(G.degree())

# sort the nodes based on degree
sorted_nodes = sorted(degrees, key=degrees.get, reverse=True)

# take the top 3 nodes with highest degree
top_nodes = sorted_nodes[:100]

# create a subgraph from the top nodes
subgraph = G.subgraph(top_nodes)
#PageRank

# def page_rank(graph):
#     pr_dict = nx.pagerank_numpy(graph)

#     for node, pr in pr_dict.items():
#         print("Node:", node, "PageRank:", pr)
pr_citations=nx.pagerank_numpy(subgraph, 0.85)

# #Co-occurence analysis

# ca = nx.overlap_weighted_communities(subgraph)

# #Out-degree
out_deg = dict(subgraph.out_degree())


# #BibliographicCoupling


# # Get a list of all nodes in the graph

# # Initialize an empty dictionary to store the bibliographic coupling values

def bib_coupling(graph):
    nodes = list(graph.nodes())

    bc_dict = {}

    # Iterate over all pairs of nodes
    for i in range(len(nodes)):
        for j in range(i+1, len(nodes)):
            
            # Compute the set of neighbors of nodes i and j
            neighbors_i = set(G.neighbors(nodes[i]))
            neighbors_j = set(G.neighbors(nodes[j]))

            # Compute the intersection of the two sets of neighbors
            common_neighbors = neighbors_i.intersection(neighbors_j)

            # Compute the bibliographic coupling between nodes i and j
            bc = len(common_neighbors)
            
            # Store the bibliographic coupling value in the dictionary
            bc_dict[(nodes[i], nodes[j])] = bc

    return bc_dict
# # # Print the dictionary of bibliographic coupling values


# print(pr_citations)
# # print(ca)
# print(out_deg)
# print(bib_coupling(subgraph))


from sklearn.metrics.pairwise import cosine_similarity

# Create a directed graph object G

# Compute the adjacency matrix of the graph
def co_occurence(G):
#     A = nx.adjacency_matrix(graph)

# # Compute the cosine similarity between all pairs of nodes
#     co_occurrence = cosine_similarity(A)

# # Print the cosine similarity between each pair of nodes
#     cos_similarity_dict={}
#     for i in range(G.number_of_nodes()):
#         for j in range(i+1, G.number_of_nodes()):
#             cos_similarity_dict[(i,j)] = co_occurrence[i,j]
    
#     return cos_similarity_dict

    co_occurrence = {}
    for i in G.nodes():
        for j in G.nodes():
            if i != j:
                count = 0
                for u, v in G.out_edges(i):
                    if v in G.successors(j):
                        count += 1
                co_occurrence[(i, j)] = count
    return co_occurrence


print(co_occurence(subgraph))

print(bib_coupling(subgraph))

print(out_deg)
print(pr_citations)

# visualize the subgraph
pos = nx.random_layout(subgraph)
fig, ax = plt.subplots(figsize=(15, 10))
nx.draw_networkx_nodes(subgraph, pos, node_color='r', node_size=100, ax=ax)
nx.draw_networkx_edges(subgraph, pos, edge_color='b', arrows=True, width=0.5, ax=ax)
nx.draw_networkx_labels(subgraph, pos, font_size=8, font_family='sans-serif', ax=ax)
ax.set_axis_off()
# plt.show()


# between_c= dict(subgraph.betweenness_centrality())
between_c_1= nx.betweenness_centrality(subgraph)
print(between_c_1)




# print(between_c==between_c_1)


# Calculate HITS scores
authority_scores, hub_scores = nx.hits(subgraph)

# Store HITS scores in a dictionary
hits_dict = {}
for node in subgraph.nodes():
    hits_dict[node] = {"Authority": authority_scores[node], "Hub": hub_scores[node]}

print(hits_dict)


# Calculate closeness centrality
closeness_c = nx.closeness_centrality(subgraph)

# Store closeness centrality scores in a dictionary
closeness_dict = {}
for node in subgraph.nodes():
    closeness_dict[node] = closeness_c[node]


print(closeness_dict)

# # Sort the dictionary based on the closeness centrality scores in descending order
# highest_scores = sorted(closeness_dict.items(), key=lambda x: x[1], reverse=True)

# # Print the top 10 movies with highest closeness centrality scores
# for node, score in highest_scores[:10]:
#     print(f"Movie: {node}, Closeness Centrality: {score}")

# lowest_scores= sorted(closeness_dict.items(), key= lambda x:x[1], reverse=False)

# for node, score in lowest_scores[:10]:
#     print(f"Movie: {node}, Closeness Centrality: {score}")
# print the nodes and edges of the subgraph
print("Nodes:", len(G.nodes()))
print("Edges:", len(G.edges()))