from flask import Flask, render_template, request, redirect
import pyperclip as pc
import datetime as dt
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate 
import os
import string
import random
#############################################################################################################
######################################### Creating SQL database #############################################


app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///' +os.path.join(basedir,"data.sqlite")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

#############################################################################################################
########################################## Model Creation ###################################################

class Url(db.Model):
    __tablename__ = 'urls'
    id = db.Column(db.Integer, primary_key = True)
    long = db.Column(db.String())
    short =db.Column(db.String(10))
    
    def __init__(self, long, short):
        self.long = long
        self.short = "http://127.0.0.1:5000/"+short
    

#############################################################################################################
def shorten_url():
    letters = string.ascii_lowercase + string.ascii_uppercase + string.digits
    while True:
        rand_letters = random.choices(letters, k=10)
        rand_letters = "".join(rand_letters)
        short_url = Url.query.filter_by(short=rand_letters).first()
        if not short_url:
            return rand_letters

###############################################Pages##########################################################

@app.route('/')
def home_get():
    return render_template("index.html")

@app.route('/', methods =["POST"])
def home_post():
    long = request.form.get("in_1") 
    found_url = Url.query.filter_by(long=long).first()
    if found_url:
        for i in db.session.execute("SELECT short FROM urls WHERE long='{}'".format(long)):
            short =i[0]
            return render_template("shorten.html" , short=short)
    else:
        short = shorten_url()
        URL = Url(long, short)
        db.session.add(URL)
        db.session.commit()
        return render_template("shorten.html" , short="http://127.0.0.1:5000/"+short)

@app.route("/short",methods=["POST"])
def copyToClipboard():
    shortenlink=request.form.get("surl")
    pc.copy(shortenlink)
    return render_template("index.html")

@app.route('/history')
def history():
    Hist = db.session.execute("Select * from urls")
    return render_template("history.html", data =Hist)

@app.route("/<short>")
def direct(short):
    for i in db.session.execute("SELECT long FROM urls WHERE short='{}'".format("http://127.0.0.1:5000/"+short)):
        return redirect(i[0])


############################################################################################################################
############################################################################################################################

if __name__ =="__main__":
    app.run(debug=True)
     










