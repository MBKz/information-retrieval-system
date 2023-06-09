from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import pickle


def getInvertedIndex(corpus,mode,dataset):

    # Create a list of documents
    file = 'indexes/'+dataset+'_index.pickle'
    documents_content = list(corpus.values())
    documents_keys = list(corpus.keys())


    if(mode == 'offline'):
        
        # Create a TfidfVectorizer object
        vectorizer = TfidfVectorizer()

        # 'l2' for normalization
        transformer = TfidfTransformer(norm='l2')

        # Fit the vectorizer to the documents
        tfidf_matrix = vectorizer.fit_transform(documents_content)

        # Normalize the TF-IDF matrix
        normalized_matrix = transformer.fit_transform(tfidf_matrix)

        # write the result on file
        with open(file, 'wb') as handle:
            pickle.dump((normalized_matrix, documents_keys, documents_content, vectorizer), handle)
            
        return file
    
    else:
        # Create a TfidfVectorizer object
        with open(file, 'rb') as handle:
            normalized_matrix, documents_keys, documents_content, vectorizer = pickle.load(handle)

        #'l2' for normalization
        transformer = TfidfTransformer(norm='l2')
       
        # Fit the vectorizer to the documents
        tfidf_matrix = vectorizer.transform(list(corpus.values()))
        
        # Normalize the TF-IDF matrix
        normalized_matrix = transformer.fit_transform(tfidf_matrix)
       
        return normalized_matrix
