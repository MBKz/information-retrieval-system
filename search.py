import requests
import json
from enum import Enum
from pydantic import BaseModel
from services.extra.Suggest import formulation ,getSuggestions
from services.second.GetInvertedIndex import getInvertedIndex
from services.second.CosineSimilarity import getSimilarity


# initialling connection
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
app.add_middleware(CORSMiddleware , allow_origins=["*"] , allow_credentials=True , allow_methods=["*"] , allow_headers=["*"])

f = open('config.json')
config = json.load(f)
f.close()

class datasets(str, Enum):
    antique    = "antique"
    wikir      = "wikir"

class Request (BaseModel):
    dataset: datasets
    query:   str


@app.post("/search")
def search(request: Request):

    # text handling
    try:
        docs = requests.post(config['textHandler']['ip']+ ":" +config['textHandler']['port']+ "/" +config['textHandler']['endPoint'] ,json=request.dict())
    except:
        print("Micro-service exception occurred")

    # inverted index (tfidf)
    query_index = getInvertedIndex(docs.json() ,"online" ,request.dataset)

    # results by similarity
    results = getSimilarity(query_index ,request.dataset)

    return results




@app.post("/suggest")
def suggest(request: Request):

    # text handling
    try:
        processed_query = requests.post(config['textHandler']['ip']+ ":" +config['textHandler']['port']+ "/" +config['textHandler']['endPoint'] ,json=request.dict())
    except:
        print("Micro-service exception occurred")

    # get queries
    with open('queries/'+request.dataset+'/queries.txt', 'r') as file:
            queries = file.readlines()

    # get queries without the IDs
    queries = [query.strip() for query in queries]
    gold_stander_queries = []
    for query in queries:
        q_split = query.split('\t')
        gold_stander_queries.append(q_split[1])
    
    suggestions = getSuggestions(processed_query.json() ,gold_stander_queries)

    return (formulation(suggestions ,request.query ,gold_stander_queries))