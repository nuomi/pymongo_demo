from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)

db = MongoClient('mongo_test', connect=False).db_test




@app.route("/")
def home():
    return "Hello World from Flask"

@app.route('/all')
def all():
    # so find() will return objects without _id 
    collection = db.collection.find({}, {'_id': False})
    print('print count')
    print(collection.count())

    return jsonify(list(collection))

@app.route('/add')
def add():
    item = {'name':'John'}
    try:
        db.collection.insert(item)
        return jsonify({'ok':1})
    except Exception as e:
        print('on /add ', e)
        return jsonify({'ok':0})

@app.route('/flush')
def flush():
    try:
        db.collection.drop()
        return jsonify({'ok':1})
    except Exception as e:
        print('on /add ', e)
        return jsonify({'ok':0})



if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)
