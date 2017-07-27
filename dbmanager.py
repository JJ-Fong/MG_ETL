import psycopg2

def connect(hostname, username, password, database):
    conn = psycopg2.connect( host=hostname, user=username, password=password, dbname=database)
    return conn

def doquery(conn, query):
    cur = conn.cursor()
    cur.execute(query)
    rec = []
    
