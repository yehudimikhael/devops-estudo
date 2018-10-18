import mysql.connector
import os
con = mysql.connector.connect(user='noc', password='concrete123..', host=os.environ.get('DB_HOST'), database='inscricao')
cur = con.cursor()

def db_select():
    cur.execute("SELECT * FROM competidores")
    result = cur.fetchall()
    return result
    con.close()