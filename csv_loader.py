import psycopg2
import json
import csv
import modmodule
from collections import defaultdict

with open('settings.json') as jfile:
    data = json.load(jfile)

with open('rdbconfig.json') as j2file:
    config = json.load(j2file)


hostname = data["hostname"]
username = data["username"]
password = data["password"]
database = data["database"]
tables = data["tables"]

flag = True

tfields = defaultdict(list) 
tconfig = config["tables"]

for t in tconfig:
    tname = t["tablename"]
    for f in t["fields"]:
        tfields[tname].append((f["name"], f["type"]))


try:    
    conn = psycopg2.connect( host=hostname, user=username, password=password, dbname=database)
except:
    print 'Unable to connecto to DB'
    flag = False

if (flag): 
    for table in tables:
        scount = 0
        fcount = 0 
        override = table["override"]
        files = table["files"]
        tablename = table["tablename"]
        cur = conn.cursor()
        if (override):
            cur.execute("DELETE FROM "+tablename)
            conn.commit()
            print tablename+" OVERRIDE COMPLETED"
        fields = []
        types = []
        for item in tfields[tablename]:
            f, t  = item
            fields.append(f)
            types.append(t)
        print fields, types 
        for f in files:
            with open(f) as csvf:
                reader = csv.DictReader(csvf, delimiter='|')
                for row in reader:
                    query = "INSERT INTO "+tablename+" ("
                    values = "" 
                    for (k,v) in row.items():
                        if k.upper() in fields:
                            query += str(k)+","
                    














                            
