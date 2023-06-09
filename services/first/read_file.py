import csv

def read_tsv_file(file_path):
    data = {}
    with open(file_path, 'r', newline='', encoding='utf-8') as tsv_file:
        reader = csv.reader(tsv_file, delimiter='\t')
        next(reader)
        for row in reader:
            data[row[0]]= row[1]
    return data


def read_csv_file(file_path):
    data = {}
    with open(file_path, mode ='r')as file:
        csvFile = csv.reader(file)
        for row in csvFile:
            data[row[0]]= row[1]
    return data

