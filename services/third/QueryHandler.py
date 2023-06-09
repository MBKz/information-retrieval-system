

# query relevant by query id
def get_relevant_docs(query_id,dataset):
    relevant_docs_path = 'goldStander/'+dataset+"/"+query_id+".txt"
    with open(relevant_docs_path, "r") as file:
        lines = file.readlines()
        relevant_docs = []
        extract_docs = False
        for line in lines:
            if line.startswith("Relevant Docs:"):
                extract_docs = True
            elif extract_docs:
                doc_id = line.strip()
                relevant_docs.append(doc_id)
    return relevant_docs

