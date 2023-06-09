please follow those steps to run the system:

# INSTALLATION
    1- install Python 3.10.4
    2- pip install the packages [ nltk , sklearn , numpy , requests , pydantic ] 
    3- download the datasets
	- wikir:   https://ir-datasets.com/wikir.html
	- antique: https://ir-datasets.com/antique.html  
    4- move the downloaded datasets to the folder "datasets"
	PS: make sure that the datasets have the names wikir.csv & antique.tsc in datasets folder

# RUNNING

    Training:
        1- uncomment the method calling in the last 2 lines in train.py file 
        2- run the code directly from train.py file using your IDE
            PS: notice that you should send the dataset name in the code while your calling the method

    Server launching:
        1- open 2 cmd's in project repository
        2- in the first cmd run the command   "~ uvicorn TextHandler:app --port 8000 --reload "
        3- in the second cmd run the command  "~ uvicorn search:app --port 8001 --host 0.0.0.0 --reload "
        4- now you can try the system out from your browser by calling " ~ 127.0.0.1:8001/docs "
        5- you can search using the api             BASE/search  {with body: query , dataset}
        6- for suggestions you can access the api   BASE/suggest {with body: query , dataset}

    Evaluation:
        for evaluating queries one by one (recall and precision):
            1- uncomment the method calling in the last line in queryEvaluate.py file 
            2- run the code directly from queryEvaluate.py file using your IDE
                PS: notice that you should send the dataset name in the code while your calling the method 

        for evaluating the system (map and mrr):
            1- uncomment the method calling in the last line in systemEvaluation.py file 
            2- run the code directly from systemEvaluation.py file using your IDE
                PS: notice that you should send the dataset name in the code while your calling the method 



Have a nice experience :)