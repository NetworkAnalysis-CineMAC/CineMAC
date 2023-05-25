import requests
import pandas as pd
import json


people_names = pd.read_csv("src/results/n2/rounded.csv", encoding="utf-8")

# list of people's names for whom we want to retrieve nationality data
people_names = set(people_names['primaryName'])
people_names = list(people_names)

people_dict = {}

node_set = people_names
json_file = "../src/datasets/nationalities.json"
json_dict = people_dict

#create the jason outside of the function so that it is not overwritten but just updated
with open(json_file, "w") as nationalities:
    json.dump(people_dict, nationalities)


def retrieveNationality(node_set, json_file, json_dict):       

    excluded = []

    no_wikidata_for_name = 0
    no_data_for_name = 0
    no_nationality_data = 0

    for name in node_set:    
        # Wikidata Query Service API endpoint for retrieving the person's identifier
        url = f'https://query.wikidata.org/sparql?query=SELECT ?item WHERE {{ ?item rdfs:label "{name}"@en. }}'
        
        # set headers to specify the response format (JSON)
        headers = {'Accept': 'application/sparql-results+json'}
        
        # request the person's identifier from WDQS API
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            data = response.json()
        
            try:
                # extract the person's Wikidata identifier from the JSON response
                person_id = data['results']['bindings'][0]['item']['value'].split('/')[-1]
                # Wikidata API endpoint for the person's data
                url = f'https://www.wikidata.org/wiki/Special:EntityData/{person_id}.json'
                # request the person's data from Wikidata API
                response = requests.get(url)
                if response.status_code == 200:
                    data = response.json()
                    # retrieve the person's nationality data from the Wikidata JSON response
                    try:
                        nationality = data['entities'][person_id]['claims']['P27'][0]['mainsnak']['datavalue']['value']['id']                    
                        json_dict[name] = {'id': person_id, 'nationality' : nationality}
                        with open(json_file, "r") as nationalities:
                            existing_data = json.load(nationalities)
                        existing_data.update(json_dict)
                        with open(json_file, "w", encoding="utf-8") as nationalities: #then set a path
                            json.dump(existing_data, nationalities, ensure_ascii=False, indent=4)
                                        
                    except KeyError:
                        no_nationality_data += 1
                else:
                    no_data_for_name += 1
            except IndexError:
                no_wikidata_for_name +=1
                excluded.append({name})
        else:
            no_data_for_name += 1
             
    print(len(no_wikidata_for_name))
    print(len(no_data_for_name))
    print(len(no_nationality_data))
    print(len(json_dict))
    return excluded


