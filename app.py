import os
from flask import Flask,request,render_template,redirect,session,send_from_directory
from db.images import fetchDataFromTable,getIDList
from dotenv import load_dotenv
parentdir = os.path.dirname(os.path.realpath(__file__))
load_dotenv(os.path.join(parentdir,'.env'))
FLASK_SECRET_KEY = os.getenv("SECRET_KEY")
imgsdir = os.path.join(parentdir, "dataset")
app=Flask(__name__)
app.secret_key=FLASK_SECRET_KEY
@app.route("/",methods=["GET","POST"])
def home():
    if request.method=="POST":
        if "play" in request.form:
            return redirect("/play")        
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
    if session['round']>3:
        session['total']+=int(session['score'])
        return redirect("/end")

    currentimgID=session['idlist'][session['round']]
    currentimg=fetchDataFromTable(currentimgID)
    imgpath=currentimg[6]
    directoryname=currentimg[2]
    media=currentimg[3]
    inspiration_lat=currentimg[7]
    inspiration_lng=currentimg[8]
    origin_lat=currentimg[9]
    origin_lng=currentimg[10]
    if request.method=="POST":
        if ((request.form['ans'].lower()).strip()==media.lower()) or ((request.form['ans'].lower()).strip()==directoryname):
            session['score']+=1
        if 'clearall' in request.form:
            session.clear()
            return redirect("/play")
        session['round']+=1
        return redirect("/play")  #to start a GET request right after the POST is over,or it'll do both simultaneously
    return render_template("game.html",score=session['score'],image=imgpath,round=int(session['round'])+1)
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
@app.route("/dataset/<path:imgpath>")
def sendurl(imgpath):
    return send_from_directory(imgsdir,imgpath)
app.run(debug=True)