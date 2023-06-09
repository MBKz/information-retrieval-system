
def toLowerCase(corpus):
    for doc_id, doc_content in corpus.items():
        corpus[doc_id] = doc_content.lower().strip()
        
    return corpus

