from nltk.tokenize import word_tokenize

def tokenizer(corpus):
    for doc_id, doc_content in corpus.items():
        corpus[doc_id] = word_tokenize(doc_content)
     
    return corpus        

