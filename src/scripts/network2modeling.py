import networkx as nx
from networkx.algorithms import bipartite
import pandas as pd

network_data = pd.read_csv("./src/datasets/network2data_madda.csv", encoding="utf-8")
", dtype={'movie_ID':'string', 'title':'string', 'movie_country':'string', 'year':'string', 'cites':'string', 'person_ID':'string', 'person_role':'string', 'nconst':'string', 'primaryName':'string', 'birthYear': 'string', 'deathYear':'string' })"
#creation of movie set

network2 = nx.Graph() 

movie_set = network_data['movie_ID'].tolist() #put the unique movie IDs in a list to add as nodes
network2.add_nodes_from(movie_set, bipartite=0)

people_set = network_data['nconst'].tolist() #put the unique people IDs in a list to add as nodes
network2.add_nodes_from(people_set, bipartite=1)


# initiate dictionaries for attributes
movies_dict = {}
people_dict = {}

#in these dict a key is a ID and the value is a dictionary with title, country, year,

for row in network_data.iterrows():   
      
    movie_key = row[1]['movie_ID']
    if network2.has_edge(row[1]['person_ID'], movie_key) == False: #checking that an edge doesn't already exist
        network2.add_edge(row[1]['person_ID'], movie_key) #adding edge

    # managing data for movie set  
    # if movie does not exist create key and append row values in inner dict        
    if movie_key not in movies_dict.keys(): 
            movies_dict[movie_key] = {'title': row[1]['title'],
                                                'country': [],
                                                'year' : row[1]['year'],
                                                'cites': []}

            movies_dict[movie_key]['country'].append(row[1]['movie_country'])
            movies_dict[movie_key]['cites'].append(row[1]['cites'])           

    else:
        # check if there's a new value for country    
        if row[1]['movie_country'] not in movies_dict[movie_key]['country']:
            movies_dict[movie_key]['country'].append(row[1]['movie_country'])

        # check if there's a new citation values
        if row[1]['cites'] not in movies_dict[movie_key]['cites']:
            movies_dict[movie_key]['cites'].append(row[1]['cites'])


    # managing data for people set

    people_key = row[1]['person_ID']

    if people_key not in people_dict.keys(): 
  
        people_dict[people_key] = {'name': row[1]['primaryName'],
                                'role': []}        
        
        people_dict[people_key]['role'].append(row[1]['person_role'])    
        
    else:
        # check if there's a new value for role    
        if row[1]['person_role'] not in people_dict[people_key]['role']:
            people_dict[people_key]['role'].append(row[1]['person_role'])


# adding attributes
nx.set_node_attributes(network2, movies_dict)
nx.set_node_attributes(network2, people_dict)

num_edges = network2.number_of_edges()
print(num_edges) #113440 edges

# trys
print(network2.nodes['tt3008816']['country'])
print(network2.nodes['tt3008816']['title'])
print(network2.nodes['tt3008816']['year'])
print(network2.nodes['tt3008816']['cites'])


# writing graphs

#converting list-type attributes in string values to write the graphs
for node in network2.nodes():
    if 'country' in network2.nodes[node]:
        network2.nodes[node]['country'] = ','.join(map(str, network2.nodes[node]['country']))
    if 'cites' in network2.nodes[node]:
        network2.nodes[node]['cites'] = ','.join(map(str, network2.nodes[node]['cites']))
    if 'role' in network2.nodes[node]:
        network2.nodes[node]['role'] = ','.join(map(str, network2.nodes[node]['role']))

#commented out because I don't need to export those networks anymore 
# this is the first one, down here I am directly projecting to get the Network we actually need
'''nx.write_graphml(network2, "bipartite.graphml")'''
nx.write_gexf(network2, "bipartite.gexf")
'''
network2proj = bipartite.projected_graph(network2, people_set)
num_edges1 = network2proj.number_of_edges()
print(num_edges1)

#here I add the movies that define collaborations as edge lables
separator= ","
for node1, node2 in network2proj.edges():
    movie_node = set(network2[node1]) & set(network2[node2])  # find the movie node connecting the two people nodes and add as edge
    network2proj.add_edge(node1, node2, label=separator.join(list(movie_node))) #ad the edge label

    

nx.write_gexf(network2proj, "./data/network2proj.gexf")'''


