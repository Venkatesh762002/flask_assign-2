from flask import Flask,request,jsonify
import os
from dotenv import load_dotenv
import pymongo

app=Flask(__name__)

load_dotenv()

MONGODB_URL=os.getenv('MONGODB_URL')
client=pymongo.MongoClient(MONGODB_URL)
db=client.stu_data
collection=db['students_data']

@app.route('/submit',methods=['POST'])
def submit():
    data=dict(request.json)
    collection.insert_one(data)
    return jsonify({"result":"Data submitted successfully"})

@app.route('/view')
def view():
    data=list(collection.find())
    
    for item in data:
        item.pop('_id')
    return jsonify({
        "data":data
    })


if __name__=='__main__':
    app.run(host='127.0.0.1',port=9000,debug=True)