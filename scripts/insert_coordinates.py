import requests
from pprint import pprint #use to make json responses readable when needed
import sqlite3
import os
from dotenv import load_dotenv
parentdir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
imgsdir = os.path.join(parentdir, "dataset")
load_dotenv(os.path.join(parentdir,'.env'))
API_KEY = os.getenv("GEOAPIFY_API_KEY")
conn=sqlite3.connect(os.path.join(parentdir,'locations.db'))
curs=conn.cursor()
def getCoordinates(location):
    parageo={'text':location,
            'api_key':API_KEY}
    reqgeocode=requests.get(r'https://api.geoapify.com/v1/geocode/search',params=parageo)
    data=reqgeocode.json()
    coordinates=data['features'][0]['geometry']['coordinates']
    return coordinates

def insertCoordinates(directoryname,inspiration_lat,inspiration_lng,origin_lat,origin_lng):
    curs.execute("""
                 UPDATE locations
                 SET inspiration_lat=?,
                 inspiration_lng=?,
                 origin_lat=?,
                 origin_lng=?
                 WHERE directoryname=?""",(inspiration_lat,inspiration_lng,origin_lat,origin_lng,directoryname))
for curr_root,dirs,items in os.walk(imgsdir):
    if items:
        parts = os.path.normpath(curr_root).split(os.sep)
        directoryname=parts[-1]
        print(directoryname)
        curs.execute("SELECT inspiration_loc,origin_loc,inspiration_lat,origin_lat FROM locations WHERE directoryname=?",(directoryname,))
        inspiration_loc,origin_loc,inspiration_lat,origin_lat=curs.fetchone()
        if inspiration_lat is not None and origin_lat is not None:
            continue
        if inspiration_loc is not None and origin_loc is not None:
            inspiration_lng, inspiration_lat = getCoordinates(inspiration_loc)
            origin_lng, origin_lat = getCoordinates(origin_loc)
        elif inspiration_loc is None and origin_loc is not None:
            inspiration_lng, inspiration_lat = None,None
            origin_lng, origin_lat = getCoordinates(origin_loc)
        elif inspiration_loc is not None and origin_loc is None:
            inspiration_lng, inspiration_lat = getCoordinates(inspiration_loc)
            origin_lng, origin_lat = None,None
        else:
            inspiration_lng, inspiration_lat = None,None
            origin_lng, origin_lat = None,None
        insertCoordinates(directoryname,inspiration_lat,inspiration_lng,origin_lat,origin_lng)
conn.commit()
conn.close()