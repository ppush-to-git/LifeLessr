import sqlite3
import os
parentdir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
imgsdir = os.path.join(parentdir, "dataset")
def getIDList():
    conn=sqlite3.connect(os.path.join(parentdir,'locations.db'))
    curs=conn.cursor()
    idlist=[]
    curs.execute("""SELECT id FROM locations 
                 ORDER BY RANDOM()
                 LIMIT 4;""")
    rows=curs.fetchall()
    for id in rows:
        idlist.append(id[0])
    conn.close()
    return idlist

def fetchData(idn):
    conn=sqlite3.connect(os.path.join(parentdir,'locations.db'))
    curs=conn.cursor()
    curs.execute("SELECT * FROM locations WHERE id=?",(idn,))
    data=curs.fetchone()
    conn.close()
    return data
