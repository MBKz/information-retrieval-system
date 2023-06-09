from nltk.stem import WordNetLemmatizer

def lemmatizer(corpus):
    lemmatizer = WordNetLemmatizer()
    lemmatizer_sentence = []

    for doc_id, doc_content in corpus.items():
        for w in doc_content:
            lemmatizer_sentence.append(lemmatizer.lemmatize(w, pos = 'v'))
        corpus[doc_id] = lemmatizer_sentence
        lemmatizer_sentence = []
        
    return corpus

