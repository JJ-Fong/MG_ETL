import psycopg2
import json

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
    #for sfile in files:
    cur = conn.cursor()
    cur.execute("SELECT * from raw_proveedores")
    rows = cur.fetchall()
    print rows
    
