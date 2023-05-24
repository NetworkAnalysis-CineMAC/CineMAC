# collaborations network averaged measure

import pandas as pd

n2_degree = pd.read_csv("src/scripts/degree.csv")
n2_closeness = pd.read_csv("src/scripts/closeness.csv")
n2_eigenvector = pd.read_csv("src/scripts/eigenvector.csv")
n2_betwenness = pd.read_csv("src/scripts/betweenness.csv")

n2_degree = n2_degree[["nconst", "measure"]]
n2_eigenvector = n2_eigenvector[["nconst", "measure"]]
n2_betwenness = n2_betwenness[["nconst", "measure"]]

#print(len(n1_in_degree))
#print(len(n1_pagerank))
'''n1_averaged = pd.merge(n1_in_degree, n1_pagerank, left_on = "tconst", right_on="tconst")
n1_averaged = pd.merge(n1_averaged, n1_betwenness, left_on="tconst", right_on="tconst")
n1_averaged = n1_averaged[["tconst", "Film", "Country", "In-Degree Centrality", "PageRank Score", "Betweenness Centrality"]]'''
#print(n1_averaged)

# normalize eigenvector column

#n1_averaged["Eigenvector Centrality"] =(n1_averaged["Eigenvector Centrality"]-n1_averaged["Eigenvector Centrality"].min())/(n1_averaged["Eigenvector Centrality"].max()-n1_averaged["Eigenvector Centrality"].min())
#print(n1_averaged["Eigenvector Centrality"])

# add average col

n1_averaged['CineMAC rank'] = n1_averaged[["In-Degree Centrality", "PageRank Score", "Betweenness Centrality"]].mean(axis=1)
n1_averaged = n1_averaged.sort_values(by='CineMAC rank', ascending=False)
cinemac = n1_averaged.drop_duplicates()
cinemac.to_csv("src/graph1-tables/N1_cineMAC_rank.csv", index=False)