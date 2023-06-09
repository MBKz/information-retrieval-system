from services.third.QueryHandler import get_relevant_docs


# for query 
def calculate_recall(query,retrieved_docs ,dataset):
    query_id = query.split('\t')[0]
    relevant_docs = get_relevant_docs(query_id ,dataset)
    relevant_and_retrieved = set(relevant_docs).intersection(set(retrieved_docs))
    recall = len(relevant_and_retrieved) / len(relevant_docs)
    return recall

def calculate_precision_at_k(query, k ,retrieved_docs ,dataset):
    query_id = query.split('\t')[0]
    relevant_docs = get_relevant_docs(query_id ,dataset)
    retrieved_docs_at_k = retrieved_docs[:k]
    relevant_and_retrieved = set(relevant_docs).intersection(set(retrieved_docs_at_k))
    precision = len(relevant_and_retrieved) / k
    return precision



# for system
def calculate_average_precision(query,retrieved_docs,dataset):
    query_id = query.split('\t')[0]
    relevant_docs = get_relevant_docs(query_id,dataset)
    average_precision = 0.0
    num_correct = 0
    precision_at_rank = []

    for i, doc in enumerate(retrieved_docs):
        if doc in relevant_docs:
            num_correct += 1
            precision = num_correct / (i + 1)
            precision_at_rank.append(precision)

    if num_correct > 0:
        average_precision = sum(precision_at_rank) / num_correct
    
    return average_precision

def calculate_mrr(query,retrieved_docs,dataset):
    query_id = query.split('\t')[0]
    relevant_docs = get_relevant_docs(query_id,dataset)
    reciprocal_ranks = []
    for result_list in retrieved_docs:
        found_relevant = False
        for i, doc_id in enumerate(retrieved_docs, start = 1):
            if doc_id in relevant_docs:
                reciprocal_ranks.append(1.0 / i)
                found_relevant = True
                break
        if not found_relevant:
            reciprocal_ranks.append(0.0)
        
    if len(reciprocal_ranks) != 0:
        mrr = sum(reciprocal_ranks) / len(reciprocal_ranks)
    else:
        mrr = 0
    return mrr