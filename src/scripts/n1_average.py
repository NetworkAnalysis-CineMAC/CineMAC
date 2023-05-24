import pandas as pd

# citations network averaged measure

n1_in_degree = pd.read_csv("src\graph1-tables\df_in_degree.csv")
n1_pagerank = pd.read_csv("src\graph1-tables\df_pagerank.csv")
n1_eigenvector = pd.read_csv("src\graph1-tables\df_eigenvector.csv")
n1_betwenness = pd.read_csv("src\graph1-tables\df_betweenness.csv")

n1_in_degree = n1_in_degree[["Film", "In-Degree Centrality","tconst", "Country", ]]
n1_pagerank = n1_pagerank[["PageRank Score", "tconst"]]
n1_betwenness = n1_betwenness[["Betweenness Centrality", "tconst"]]

#print(len(n1_in_degree))
#print(len(n1_pagerank))
n1_averaged = pd.merge(n1_in_degree, n1_pagerank, left_on = "tconst", right_on="tconst")
n1_averaged = pd.merge(n1_averaged, n1_betwenness, left_on="tconst", right_on="tconst")
n1_averaged = n1_averaged[["tconst", "Film", "Country", "In-Degree Centrality", "PageRank Score", "Betweenness Centrality"]]
#print(n1_averaged)

# normalize eigenvector column

#n1_averaged["Eigenvector Centrality"] =(n1_averaged["Eigenvector Centrality"]-n1_averaged["Eigenvector Centrality"].min())/(n1_averaged["Eigenvector Centrality"].max()-n1_averaged["Eigenvector Centrality"].min())
#print(n1_averaged["Eigenvector Centrality"])

# add average col

n1_averaged['CineMAC rank'] = n1_averaged[["In-Degree Centrality", "PageRank Score", "Betweenness Centrality"]].mean(axis=1)
n1_averaged = n1_averaged.sort_values(by='CineMAC rank', ascending=False)
cinemac = n1_averaged.drop_duplicates()
cinemac.to_csv("src/graph1-tables/N1_cineMAC_rank.csv", index=False)


# Drop rows where the specific column has the same value
for idx, row in cinemac.iterrows():
    if cinemac.at[idx, "Country"] == "USA":
        cinemac.drop(index=idx, axis=0, inplace=True)

east_asian_rank = cinemac
east_asian_rank.to_csv("src/graph1-tables/N1_cineMAC_ea_rank.csv")

