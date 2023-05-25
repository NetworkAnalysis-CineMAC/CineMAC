import pandas as pd
from pprint import pprint

df = pd.read_csv("src/results/n2/N2_noprod_rank_top20.csv")

# Function to round the values to two decimal places
def round_decimals(value):
    return round(value, 3)

# Apply the function to each column
df["Degree centrality"] = df["Degree centrality"].apply(round_decimals)
df["Eigenvector centrality"] = df["Eigenvector centrality"].apply(round_decimals)
df["Closeness centrality"] = df["Closeness centrality"].apply(round_decimals)
df["Betweenness centrality"] = df["Betweenness centrality"].apply(round_decimals)
df["CineMAC rank"] = df["CineMAC rank"].apply(round_decimals)

df = df.drop(columns="nconst", axis=1)
print(df)

df.to_csv("src/results/n2/rounded_nopord.csv")