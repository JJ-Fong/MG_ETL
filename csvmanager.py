import csv

reader = None

def openCSV(filename):
    with open(filename, 'rb') as csvfile:
        reader = csv.DictReader(csvfile, delimiter='|')
        return reader

def getCSVFields():
    return reader.fieldnames
