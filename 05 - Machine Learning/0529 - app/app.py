import warnings
warnings.filterwarnings("ignore")
import pickle
from flask import Flask, request, app, jsonify, url_for, render_template
from flask import Response
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression


app = Flask(__name__)
model : LinearRegression = pickle.load(open('05 - Machine Learning/models/0528_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api', methods=['POST']) # routing
def predict_api():                           # define main function ()
    '''
    For direct API calls through request.
    Function takes in json data and predicts continues value based on our model "0528_model.pkl"
    '''
    data = request.json['data']              # {"data" :{"Frequency": 9,"Angle of attack": 8,"Chord length": 10,"Free-stream velocity": 1,"Scution side": 0.002663}}
    print("Inserted data from given json", data)

    new_data = [list(data.values())]         # we need 2D array
    print("Parsed values into list", new_data)
    pred :list = model.predict(new_data)     # predicted value in list
    output = pred[0]                         # predicted value itself

    print("model.predict():", pred)
    print("model.predict()[0]:", output)
    return jsonify(output)

@app.route('/predict', methods=['POST'])     # routing
def predict():                               # define main function ()
    '''
    For direct API calls through request.
    Function takes in json data and predicts continues value based on our model "0528_model.pkl"
    '''
    data = [float(x) for x in request.form.values()]             # {"data" :{"Frequency": 9,"Angle of attack": 8,"Chord length": 10,"Free-stream velocity": 1,"Scution side": 0.002663}}
    print("Inserted data from given json", data)
    final_features = [np.array(data)]        # we need 2D array
    print("Parsed values into list", final_features)
    pred :list = model.predict(final_features)     # predicted value in list
    output = pred[0]                         # predicted value itself

    print("model.predict():", pred)
    print("model.predict()[0]:", output)


    return render_template('home.html', prediction_text = "Airfoil pressure is: {}".format(pred[0]))

if __name__ == '__main__':
    app.run(debug=True)