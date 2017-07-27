import csv

csvfile = open('Data/proveedores.csv','rb')
reader = csv.reader(csvfile, delimiter=',')

header = reader.next()
print header

csvfile.close()
