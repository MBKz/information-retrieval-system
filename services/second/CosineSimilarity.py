import pickle
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


def getSimilarity(query_index ,dataset):
    # get doc index
    file = 'indexes/'+dataset+'_index.pickle'
    with open(file, 'rb') as handle:
        normalized_matrix, documents_keys, documents_content, vectorizer = pickle.load(handle)

    # calculate similarity
    query_vector = query_index.reshape(1,-1)

    # Calculate cosine similarity between the query vector and document vectors
    cosine_similarities = cosine_similarity(query_vector, normalized_matrix)

    # Flatten the cosine similarities array
    cosine_similarities = np.ravel(cosine_similarities)

    # Get the indices that would sort the cosine similarities array in descending order
    indices = np.argsort(cosine_similarities)[::-1]

    # Rank the documents keys based on cosine similarity
    ranked_documents_keys = [documents_keys[i] for i in indices]

    # Rank the documents values based on cosine similarity
    ranked_documents_values = [documents_content[i] for i in indices]

    # formate result
    results = []
    for i, document_ID in enumerate(ranked_documents_keys):
        similarity = cosine_similarities[indices[i]]
        if similarity > 0.4:
            document_Content = ranked_documents_values[i]
            rank = i+1
            results.append({ 
                'rank': rank, 
                'document_ID': document_ID, 
                'document_Content': document_Content, 
                'similarity': similarity
            })

    return results