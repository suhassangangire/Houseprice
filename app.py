from copyreg import pickle


import pickle
from xml.sax.handler import property_interning_dict
from flask import Flask,request,app,jsonify,url_for,render_template
import numpy as np
import pandas as pd

app=Flask(__name__)
model=pickel.load(open('sub1111.csv',rb))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api',methoda=['post'])

def predict_api():
    data=request.json['data']
    print(data)
    print(np.array(list(data.values())).reshape(1,-1))
    new_data=scalar.transform(np.array(list(data.values())).reshape(1,-1))
    output=regmodel.predict(new_data)
    print(output[0])
    return jsonify(output[0])


