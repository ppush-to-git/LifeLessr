import os 
from flask import Flask,request,render_template,redirect,session
import random
parentdir = os.path.dirname(os.path.realpath(__file__))
imgfolder=os.path.join(parentdir,r"static\images")
imagepool={}

for curr_root,dirs,items in os.walk(imgfolder):
    if items!=[]:
        media=os.path.basename(curr_root)
        imagepool[media]=items

def getImages():
    currentpool=[]
    media=random.sample(list(imagepool.keys()),4)
    for med in media:
        currentpool.append((med,random.choice(imagepool[med])))
    return currentpool

app=Flask(__name__)
app.secret_key="randoms"
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
    if 'pool' not in session:
        session['pool']=getImages()
    if 'total' not in session:
        session['total']=0
    if session['round']>3:
        session['total']+=int(session['score'])
        return redirect("/end")
    imgpool=session.get('pool')
    media,img=imgpool[session['round']]
    image=f"images/{media}/{img}"
    if request.method=="POST":
        if (request.form['ans'].lower()).strip()==media:
            session['score']+=1
        if 'clearall' in request.form:
            session.clear()
            return redirect("/play")
        session['round']+=1
        return redirect("/play")  #to start a GET request right after the POST is over,or it'll do both simultaneously
    return render_template("game.html",score=session['score'],image=image,round=int(session['round'])+1)
@app.route("/end",methods=['GET','POST'])
def postgame():
    if request.method=='POST':
        if 'home' in request.form:
            session.clear()
            return redirect('/')
        if 'again' in request.form: 
            session.pop('round')
            session.pop('pool')
            session.pop('score')
            return redirect('/play')
    return render_template("postgame.html",curscore=session['score'],totalscore=session['total'])
app.run(debug=True)