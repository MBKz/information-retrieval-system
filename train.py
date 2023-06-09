from services.first.Lemmatizer import lemmatizer
from services.first.RemoveStopWords import removeStopWords
from services.first.Stemmer import stemmer
from services.first.ToLowerCase import toLowerCase
from services.first.Tokenizer import tokenizer
from services.first.read_file import read_tsv_file ,read_csv_file
from services.second.GetInvertedIndex import getInvertedIndex
import os


def train(dataset):
    print('reading corpus...')
    if(dataset == 'antique'): corpus = read_tsv_file('datasets/'+dataset+'.tsv')
    else: corpus = read_csv_file('datasets/'+dataset+'.csv')
    

    print('corpus toLowerCase ...')
    corpus = toLowerCase(corpus)

    print('corpus tokenizer ...')
    corpus = tokenizer(corpus)


    print('corpus removeStopWords ...')
    corpus = removeStopWords(corpus)

    print('corpus stemmer ...')
    corpus = stemmer(corpus)

    print('corpus lemmatizer ...')
    corpus = lemmatizer(corpus)


    # join results 
    for doc_id ,doc_content in corpus.items():
        corpus[doc_id] = " ".join(doc_content)
    print('finished text handling.')

    # inverted index (tfidf)
    query_index = getInvertedIndex(corpus,"offline",dataset)

    print("The model "+ dataset +" has been trained successfully")





def getGoldStander(dataset):

    # Specify the paths to the qrels.txt and queries.txt files
    qrels_path = r'queries/'+dataset+'/qrels.txt'
    queries_path = r'queries/'+dataset+'/queries.txt'

    # Create a directory to store the relevant files for each query
    output_dir = r'goldStander/'+dataset
    os.makedirs(output_dir, exist_ok=True)

    # Read the qrels.txt file
    with open(qrels_path, "r", encoding="utf-8") as file:
        qrels_data = file.readlines()

    # Read the queries.txt file
    with open(queries_path, "r", encoding="utf-8") as file:
        queries_data = file.readlines()

    # Create a dictionary to store relevant files for each query
    relevant_files = {}

    # Process the qrels data and map relevant files to each query
    for line in qrels_data:
        query_id, _, doc_id, _ = line.strip().split()
        
        # Construct the complete document ID in the format of "queryID_docID"
        complete_doc_id = f"{doc_id}"
        
        # Check if the query ID already exists in the dictionary
        if query_id not in relevant_files:
            relevant_files[query_id] = []
        
        # Add the complete document ID to the list of relevant files for the query
        relevant_files[query_id].append(complete_doc_id)

    # Process the queries data and store the relevant files in separate text files
    for line in queries_data:
        query_id, query_text = line.strip().split("\t")
        
        # Check if the query ID exists in the relevant files dictionary
        if query_id in relevant_files:
            # Generate a filename based on the query ID
            filename = f"{query_id}.txt"
            
            # Get the list of relevant files for the query
            relevant_docs = relevant_files[query_id]
            
            # Create the file path
            file_path = os.path.join(output_dir, filename)
            
            # Write the query text and relevant files to the file
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(f"Query ID: {query_id}\n")
                file.write(f"Query Text: {query_text}\n")
                file.write("Relevant Docs:\n")
                for doc in relevant_docs:
                    file.write(f"{doc}\n")

    return print("Gold stander queries for "+ dataset +" created successfully")



# datasets : antique - wikir
print("This might take a few minutes ,Please wait ...") 
# train('')
# getGoldStander('')