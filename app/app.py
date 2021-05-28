import json, requests
from flask import Flask, jsonify
from pycoingecko import CoinGeckoAPI
import pymongo
from pymongo import MongoClient

app = Flask(__name__)

cg = CoinGeckoAPI()
dbclient = MongoClient(host='testmongodb', port=27017)

@app.route('/get_db')
def get_database():
    
    db = dbclient['coinsdb']
    return db

@app.route('/')
def index():
    res = cg.ping()
    print ("HELLO \n----------------------")
    return res, 200



@app.route('/coins')
def coins():
    db = dbclient['coinsdb']

    records = jsonify(cg.get_coins_list())
    for rec in records.values():
        db.insert_one(rec)
    return records, 200


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='8080')
