import os
import json
import sqlite3
import pathlib
parentdir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
imgsdir = os.path.join(parentdir, "dataset")
conn=sqlite3.connect(os.path.join(parentdir,'locations.db'))
curs=conn.cursor()
def createTable():
    curs.execute("""
    CREATE TABLE IF NOT EXISTS locations(
    id INTEGER PRIMARY KEY,
    category TEXT,
    directoryname TEXT,
    media TEXT,
    inspiration_loc TEXT,
    origin_loc TEXT,
    img_path TEXT,
    inspiration_lat REAL,
    inspiration_lng REAL,
    origin_lat REAL,
    origin_lng REAL)
    """)

def addToTable(category,directoryname,media,img_path,inspiration_loc,origin_loc):
    curs.execute("""
    INSERT INTO locations(category,directoryname,media,img_path,inspiration_loc,origin_loc)
    VALUES(?,?,?,?,?,?)
    """,(category,directoryname,media,img_path,inspiration_loc,origin_loc))

def resetTable():
    curs.execute("DELETE FROM locations")
    conn.commit()
def importMetadata():
    for curr_root,dirs,items in os.walk(imgsdir):
        if items!=[]:
            parts = os.path.normpath(curr_root).split(os.sep)
            directoryname=parts[-1]
            metadatapath=os.path.join(curr_root, "metadata.json")
            with open(metadatapath,'r') as f:
                metadata=json.load(f)
            for item in items:
                img_path=pathlib.Path(curr_root+os.sep+item)
                if img_path.suffix.lower() not in [".png", ".jpg", ".jpeg", ".webp"]:
                    continue
                img_path = os.path.relpath(img_path, imgsdir).replace("\\","/")
                addToTable(metadata['category'],directoryname,metadata['media'],img_path,metadata['inspiration_loc'],metadata['origin_loc'])
createTable()
resetTable()
importMetadata()
conn.commit()
conn.close()
