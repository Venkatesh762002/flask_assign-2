from flask import Flask,request,jsonify,render_template
import json
import requests

BACKEND_URL='http://127.0.0.1:9000'

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit',methods=['POST'])
def submit():
    data=dict(request.form)
    requests.post(BACKEND_URL + '/submit',json=data)
    return "data submitted successfully..."
# @app.route('/getdata')
# def getdata():
#     response=requests.get(BACKEND_URL + '/view')
#     return response.json()

if __name__=="__main__":
    app.run(host='127.0.0.1',port=8000,debug=True)