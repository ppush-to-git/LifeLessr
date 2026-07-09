import os
from flask import Flask,request,render_template,redirect,session,send_from_directory
from db.images import fetchData,getIDList
from dotenv import load_dotenv
from helpers.distance import haversine
from helpers.scoring import calcScore
parentdir = os.path.dirname(os.path.realpath(__file__))
load_dotenv(os.path.join(parentdir,'.env'))
FLASK_SECRET_KEY = os.getenv("SECRET_KEY")
imgsdir = os.path.join(parentdir, "dataset")
app=Flask(__name__)
app.secret_key="FLASK_SECRET_KEY"
@app.route("/",methods=["GET","POST"])
def home():
    if request.method=="POST":
        if "play" in request.form:
            return redirect("/play")
        if "rules" in request.form:
            return redirect('rules')  
    return render_template("home.html")
@app.route("/play",methods=["GET","POST"])
def game():
    if 'score' not in session:
        session['score']=0
    if 'round' not in session:
        session['round']=0
    if 'idlist' not in session:
        session['idlist']=getIDList()
    if 'total' not in session:
        session['total']=0
    
    currentimgID=session['idlist'][session['round']]
    currentimg=fetchData(currentimgID)
    imgpath=currentimg[6]
    if request.method=="POST":
        session['lat']=request.form['lat']
        session['lng']=request.form['lng']
        if 'clearall' in request.form:
                session.clear()
                return redirect("/play")
        if request.form['lat']=='':
            return redirect('/play')
        return redirect('/postround')
    return render_template("game.html",score=session['score'],image=imgpath,round=int(session['round'])+1)
@app.route("/postround",methods=['GET','POST'])
def postround():
    lat=session['lat']
    lng=session['lng']
    currentimgID=session['idlist'][session['round']]
    currentimg=fetchData(currentimgID)
    media=currentimg[3]
    print(media)
    inspiration_lat=currentimg[7]
    inspiration_lng=currentimg[8]
    origin_lat=currentimg[9]
    origin_lng=currentimg[10]
    if inspiration_lat is None:
        distance=haversine(session['lat'],session['lng'],origin_lat,origin_lng)
        message=f"Spit yo shi indeed Yo guess is {distance} kms away from the origin."
        latans=origin_lat
        lngans=origin_lng
    else:
        distance_origin=haversine(session['lat'],session['lng'],origin_lat,origin_lng)
        distance_inspiration=haversine(session['lat'],session['lng'],inspiration_lat,inspiration_lng)
        if distance_inspiration<=distance_origin:
            distance=distance_inspiration
            message=f"Spit yo shi indeed Yo guess is {distance} kms away from the inspiration."
            latans=inspiration_lat
            lngans=inspiration_lng
        elif distance_origin<distance_inspiration:
            distance=distance_origin
            message=f"Spit yo shi indeed Yo guess is {distance} kms away from the origin."
            latans=origin_lat
            lngans=origin_lng
    roundscore=calcScore(distance)
    if request.method=="POST":
        session['score']+=roundscore  
        if 'clearall' in request.form:
            session.clear()
            return redirect("/play")
        if 'nextround' in request.form:
            session['round']+=1
            if session['round']>3:
                session['total']+=int(session['score'])
                return redirect("/end")
            return redirect("/play")
        session['score']+=roundscore    
    return render_template("postround.html",message=message,latans=latans,lngans=lngans,latuser=lat,lnguser=lng,roundscore=roundscore,media=media)
@app.route("/end",methods=['GET','POST'])
def postgame():
    if request.method=='POST':
        if 'home' in request.form:
            session.clear()
            return redirect('/')
        if 'again' in request.form: 
            session.pop('round')
            session.pop('idlist')
            session.pop('score')
            return redirect('/play')
    return render_template("postgame.html",curscore=session['score'],totalscore=session['total'])
@app.route('/rules',methods=['GET','POST'])
def rules():
    if request.method=='POST':
        if 'play' in request.form:
            return redirect('/play')
    return render_template('rules.html')
@app.route("/dataset/<path:imgpath>")
def sendurl(imgpath):
    return send_from_directory(imgsdir,imgpath)
app.run(debug=True)