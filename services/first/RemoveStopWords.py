
from nltk.corpus import stopwords

def removeStopWords(corpus):
    stop_words = set(stopwords.words('english')+[':','`','``','!','#','$','%','^','&','*','-','+','?','/','~',']','[','}','{','"', '""',"''", "'",'.','..',',','|','(',')'])
                 
    filtered_sentence = []
    for doc_id, doc_content in corpus.items():
        for w in doc_content:
            if w not in stop_words:
                filtered_sentence.append(w)
        corpus[doc_id] = filtered_sentence
        filtered_sentence = []
     
    return corpus

