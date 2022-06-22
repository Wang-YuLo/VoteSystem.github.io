from verified import verified
import flask
from flask import render_template,jsonify,request
from crypt import rc4_algorithm
import os
import pathlib
import json

SRC_PATH =  pathlib.Path(__file__).parent.absolute()
UPLOAD_FOLDER = os.path.join(SRC_PATH, 'uploads')


app = flask.Flask(__name__)

@app.route("/home")
def home():
    return render_template('home.html')



@app.route("/verify.html")
def verify():
    return render_template("verify.html", value='0')



@app.route("/submit", methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        if request.values['send'] == '送出':
            id = request.values.get("id")
            name = request.values.get("name")
            img = request.files['img']
            key = rc4_algorithm("encrypt","B09605029")
        if img.filename != '':
            img.save(os.path.join(UPLOAD_FOLDER, img.filename))
            img_path = os.path.join(UPLOAD_FOLDER, img.filename)

            if(verified(id,name,img_path,key)) :        
                return render_template('verify.html',passw=key,value='1')
            else:
                return render_template('verify.html',value='2') 
    else:
        return render_template('verify.html',value='2') 

@app.route("/vote.html")
def vote():
    return render_template("vote.html",voted='0')

@app.route("/vote", methods=['GET', 'POST'])
def voting():
    if request.method == 'POST':
        if request.values['send'] == '確認投票':
            with open("data.json", 'r') as f:
                    data = json.load(f)
            result = request.values.get('people')
            password = request.values.get('passw')
            if(password in data["password"] ):
                return render_template('vote.html',voted='2')
            else:
                data['password'].append(password)
                if(result=="1"):
                    data["vote"]["No.1"] +=1
                    with open('data.json','w',encoding='utF8') as f:
                        json.dump(data,f,indent=4)
                elif(result=="2"):
                    data["vote"]["No.2"] +=1
                    with open('data.json','w',encoding='utF8') as f:
                        json.dump(data,f,indent=4)
                
                return render_template('vote.html',voted='1')
    
    

if __name__ == '__main__':
    app.run(host='0.0.0.0',port='5000')