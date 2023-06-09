import requests
import json
from services.third.statistics import calculate_average_precision ,calculate_mrr

f = open('config.json')
config = json.load(f)
f.close()

def systemEvaluation(dataset: str):

    print("This might take a few minutes ,Please wait ...")   
    map_result = 0
    mmr_result = 0
   # loop on gold stander queries
    with open('queries/'+dataset+'/queries.txt', 'r') as file:
        queries = file.readlines()

    queries = [query.strip() for query in queries]
    for query in queries:
        # search about the query
        q_split = query.split('\t')

        try:
            docs = (requests.post(config['search']['ip']+ ":" +config['search']['port']+ "/" +config['search']['endPoint'] 
                                ,json = {"dataset":dataset, "query":q_split[1]} )).json()
        except:
            print("\nMicro-service exception occurred\n")

        # get docs retrieved ids
        retrieved_docs = []
        for i, doc in enumerate(docs):
            retrieved_docs.append(doc["document_ID"])

        map_result += calculate_average_precision(query,retrieved_docs,dataset)
        mmr_result += calculate_mrr(query,retrieved_docs,dataset)

    return print({"MAP valuation result":map_result / len(queries) , "MMR valuation result":mmr_result / len(queries)})




# datasets: antique - wikir
# systemEvaluation('')