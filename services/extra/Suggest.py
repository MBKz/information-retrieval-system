import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer, TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.neighbors import NearestNeighbors



def getSuggestions(processed_query ,gold_stander_queries):

    vectorizer = TfidfVectorizer()
    transformer = TfidfTransformer()

    print("8888888888888888888888888   ")
    print(processed_query)
    # Create a query list
    query_list = list(processed_query.values())


    # Fit the vectorizer to the documents
    tfidf_query_matrix = vectorizer.fit_transform(query_list)

    # 'l2' for normalization
    transformer = TfidfTransformer(norm='l2')

    # Normalize the TF-IDF matrix
    user_input_vector = transformer.fit_transform(tfidf_query_matrix)

    # Create a query list
    query_list = list(gold_stander_queries)

    # Fit the vectorizer to the documents
    tfidf_query_matrix = vectorizer.transform(query_list)

    # Normalize the TF-IDF matrix
    query_vectors = transformer.fit_transform(tfidf_query_matrix)

    cosine_similarities = cosine_similarity(user_input_vector, query_vectors)

    # Get the indices of the nonzero values in the cosine similarity matrix
    nonzero_indices = np.nonzero(cosine_similarities.flatten())[0]

    # Retrieve the nonzero query suggestions
    return [gold_stander_queries[i] for i in nonzero_indices]



def formulation(query_suggestions ,user_input ,gold_stander_queries):
    if len(query_suggestions) > 0:
        # Create a corpus including both the historical queries and the user input
        corpus = gold_stander_queries + [user_input]

        # Convert the corpus to a term frequency matrix
        count_vectorizer = CountVectorizer()
        tf_matrix = count_vectorizer.fit_transform(corpus)

        # Use Nearest Neighbors to find the most similar queries to the user input
        n_neighbors = 4
        nn_model = NearestNeighbors(n_neighbors=n_neighbors, algorithm='brute', metric='cosine')
        nn_model.fit(tf_matrix)

        # Find the nearest neighbors to the user input
        _, nearest_indices = nn_model.kneighbors(tf_matrix[-1])

        # Retrieve the nearest queries
        return [corpus[i] for i in nearest_indices.flatten() if i < len(corpus)-1]
    
    return []