from flask import Flask, jsonify, request, abort
from flask_cors import CORS
from flask_restful import Resource, Api
import random

app = Flask(__name__)
api = Api(app)
CORS(app) 

kulitkerangajaib = [
    'serang dia!',
    'berlarilah!',
    'aku jelek dan aku bangga',
    'apakah mayones termasuk instrumen?',
    'aye aye captain!',
    'curi resep rahasia itu!',
    'COKKLATT!!',
    'gws',
    'coba tanyakan saja pada rumput yang bergoyang',
    'mungkin suatu hari'
]

@app.route('/pujakerangajaib', methods=['GET'])
@app.route('/pujakerangajaib/<name>', methods=['GET'])
def kerangajaib2(name=None):
    if name == None:
        return jsonify(random.choice(kulitkerangajaib))
    else:
        pesanname = (name+", "+random.choice(kulitkerangajaib))
        return jsonify(pesanname)

@app.route('/welcome/<name>', methods=['POST'])
def welkum(name):
    return jsonify("Selamat datang "+ name +", anda berhasil masuk ke puja kerang ajaib!")

if __name__ == "__main__":
    app.run(host="0.0.0.0")