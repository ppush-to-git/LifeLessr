from flask import Flask,request,render_template,redirect,session
import math
def haversine(latuser,lnguser,latans,lngans):
    latuser=float(latuser)
    lnguser=float(lnguser)
    latans=float(latans)
    lngans=float(lngans)
    dLat = (latuser-latans)*math.pi/180.0
    dLng = (lnguser-lngans)*math.pi/180.0
    latans = (latans)*math.pi/180.0
    latuser = (latuser)*math.pi/180.0
    a = (pow(math.sin(dLat / 2),2)+pow(math.sin(dLng/2),2)*math.cos(latans)*math.cos(latuser));
    rad = 6371
    c = 2*math.asin(math.sqrt(a))
    return round(rad*c,2)
app=Flask(__name__)
@app.route("/",methods=["GET","POST"])
def maptest():
    if request.method=="POST":
            lat=request.form['lat']
            lng=request.form['lng']
            distance_origin=haversine(lat,lng,origin_lat,origin_lng)
            distance_inspiration=haversine(lat,lng,inspiration_lat,inspiration_lng)
            message=f"Spit yo shi indeed\n Yo shi is {distance} kms away"
            return render_template("postround.html",message=message,latans=latans,lngans=lngans,latuser=lat,lnguser=lng)
    return render_template('leaflet.html')
app.run(debug=True)