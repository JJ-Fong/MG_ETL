import psycopg2
import json
import csv
from collections import defaultdict

with open('settings.json') as jfile:
    data = json.load(jfile)

hostname = data["hostname"]
username = data["username"]
password = data["password"]
database = data["database"]
tables = data["tables"]

try:    
    conn = psycopg2.connect( host=hostname, user=username, password=password, dbname=database)
except:
    print 'Unable to connecto to DB'
    
for table in tables:
    override = table["override"]
    files = table["files"]
    tablename = table["tablename"]
    cur = conn.cursor()
    #cur.execute("SELECT * from "+tablename)
    if (override):
        cur.execute("DELETE FROM "+tablename)
        conn.commit()
        print tablename+" OVERRIDE COMPLETED" 
    #Table to fill     
    if (tablename == "raw_proveedores"):
        for sfile in files:
            csvf = open(sfile, 'rb')
            reader = csv.DictReader(csvf, delimiter='|')
            fnames = reader.fieldnames
            ffnames = filter(lambda x : x not in [',', ''], fnames)

            columns = defaultdict(list)
            i = 0
            for row in reader:
                print i
                i = i + 1
                for (k,v) in row.items():
                    if k in ffnames:
                        #print k,',',v
                        columns[k].append(v)
            print columns
    if (tablename == "raw_compradores"):
        print "compradores"
    if (tablename == "raw_adjudicaciones"): 
        print "adjudicaciones"
    
