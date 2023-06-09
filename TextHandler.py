from services.first.RemoveStopWords import removeStopWords
from services.first.Lemmatizer import lemmatizer
from services.first.Stemmer import stemmer
from services.first.ToLowerCase import toLowerCase
from services.first.Tokenizer import tokenizer
from pydantic import BaseModel


# initialling connection
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
app.add_middleware(CORSMiddleware , allow_origins=["*"] , allow_credentials=True , allow_methods=["*"] , allow_headers=["*"])


class Request (BaseModel):
    query:   str


@app.post("/textHandler")
async def textHandler(request : Request): 
    corpus = {}
    corpus['query'] = request.query
    corpus = toLowerCase(corpus)
    corpus = tokenizer(corpus)
    corpus = removeStopWords(corpus)
    corpus = stemmer(corpus)
    corpus = lemmatizer(corpus)

    # join results 
    for doc_id ,doc_content in corpus.items():
        corpus[doc_id] = " ".join(doc_content)

    return corpus