import requests
import json
from services.third.statistics import calculate_precision_at_k, calculate_recall

f = open('config.json')
config = json.load(f)
f.close()

def queryEvaluation(dataset: str):
    print("This might take a few minutes ,Please wait ...")   

    # loop on gold stander queries
    with open('queries/'+dataset+'/queries.txt', 'r') as file:
        queries = file.readlines()

    queries = [query.strip() for query in queries]
    for query in queries:
        # search about the query
        try:
            docs = (requests.post(config['search']['ip']+ ":" +config['search']['port']+ "/" +config['search']['endPoint'] 
                                ,json = {"dataset":dataset, "query":query.split('\t')[1]} )).json()
        except:
            print("\nMicro-service exception occurred\n")

        # get docs retrieved ids
        retrieved_docs = []
        for i, doc in enumerate(docs):
            retrieved_docs.append(doc["document_ID"])
    
        # get recall
        recall = calculate_recall(query,retrieved_docs ,dataset)

        # get precision
        precision = calculate_precision_at_k(query, 10 ,retrieved_docs ,dataset)

        #print results
        print({'query' : query ,"recall" : recall ,"precision" : precision})

    return print("\nFinished calculating statistics for gold stander queries successfully.\n")





# datasets: antique - wikir
# queryEvaluation('')