import warnings
warnings.filterwarnings("ignore")
import pickle
from flask import Flask, request, app, jsonify
from flask import Response
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression


app = Flask(__name__)
model : LinearRegression = pickle.load(open('05 - Machine Learning/models/0528_model.pkl', 'rb'))

@app.route('/predict_api', methods=['POST'])
def predict_api():
    '''
    For direct API calls through request
    '''
    data = request.json['data']
    print(data)
    new_data = [list(data.values())]
    pred :list = model.predict(new_data)
    output = pred[0]
    return jsonify(output)

if __name__ == '__main__':
    app.run(debug=True)