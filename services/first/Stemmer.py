from nltk.stem import PorterStemmer

def stemmer(corpus):
    filtered_sentence_stem = []
    ps = PorterStemmer()

    for doc_id, doc_content in corpus.items():
        for w in doc_content:
            filtered_sentence_stem.append(ps.stem(w))
        corpus[doc_id] = filtered_sentence_stem
        filtered_sentence_stem = []
    
    return corpus

