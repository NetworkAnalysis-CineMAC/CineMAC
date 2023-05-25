# collaborations network averaged measure

import pandas as pd
from pprint import pprint

n2_degree = pd.read_csv("src/results/n2/degree.csv")
n2_closeness = pd.read_csv("src/results/n2/closeness.csv")
n2_eigenvector = pd.read_csv("src/results/n2/eigenvector.csv")
n2_betwenness = pd.read_csv("src/results/n2/betweenness.csv")

n2_closeness = n2_closeness.rename(columns={"measure": "Closeness centrality"})
n2_degree = n2_degree[["nconst", "measure"]].rename(columns={"measure": "Degree centrality"})
n2_eigenvector = n2_eigenvector[["nconst", "measure"]].rename(columns={"measure": "Eigenvector centrality"})
n2_betwenness = n2_betwenness[["nconst", "measure"]].rename(columns={"measure": "Betweenness centrality"})

# merging dfs
n2_averaged = pd.merge(n2_betwenness, n2_closeness, left_on = "nconst", right_on="nconst")
n2_averaged = pd.merge(n2_averaged, n2_degree, left_on="nconst", right_on="nconst", how="inner")
n2_averaged = pd.merge(n2_averaged, n2_eigenvector, left_on="nconst", right_on="nconst", how="inner")
n2_averaged = n2_averaged[["nconst", "name", "roles", "Degree centrality", "Eigenvector centrality","Closeness centrality", "Betweenness centrality"]]

n2_averaged = n2_averaged.drop_duplicates()

# weighted average
def weighted_average(df, path):
    
    # substitute each measure with its weighted value
    df['Degree centrality'] = df['Degree centrality'] * 0.1
    df['Eigenvector centrality'] = df['Eigenvector centrality'] * 0.2
    df['Closeness centrality'] = df['Closeness centrality'] * 0.3
    df['Betweenness centrality'] = df['Betweenness centrality'] * 0.4

    # add new weighted_average col
    df['CineMAC rank'] = df[["Degree centrality", "Eigenvector centrality", "Closeness centrality", "Betweenness centrality"]].mean(axis=1)
    df = df.sort_values(by='CineMAC rank', ascending=False)
    pprint(df[:20])
    df.to_csv(path)
    return df

weighted_df = weighted_average(n2_averaged, "src/scripts/N2_cineMAC_rank.csv")

# see what happens taking out producers
for idx, row in weighted_df.iterrows():
    if weighted_df.at[idx, "roles"] == "producer":
        weighted_df.drop(index=idx, axis=0, inplace=True)

print(weighted_df)

weighted_df.to_csv("src/scripts/N2_noprod_rank.csv")
