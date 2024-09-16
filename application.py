import pickle
from flask import Flask, request, jsonify, render_template
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

application = Flask(__name__)
app = application

# Import ridge regression model and standard scaler pickle
ridge_model = pickle.load(open('Models/ridge.pkl', 'rb'))
standard_scaler = pickle.load(open('Models/scaler.pkl', 'rb'))

# Route for homepage
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'POST':
        Temperature = float(request.form.get('Temperature'))
        Relative_Humidity = float(request.form.get('Relative Humidity'))
        Wind_Speed = float(request.form.get('Wind Speed'))
        Rainfall = float(request.form.get('Rainfall'))
        FFMC = float(request.form.get('Fine Fuel Moisture Code'))
        DMC = float(request.form.get('Duff Moisture Code'))
        ISI = float(request.form.get('Initial Spread Index'))
        Classes = float(request.form.get('Classes'))
        Region = float(request.form.get('Region'))

        # Scaling the input data
        new_data_scaled = standard_scaler.transform([[Temperature, Relative_Humidity, Wind_Speed, Rainfall, FFMC, DMC, ISI, Classes, Region]])
        result = ridge_model.predict(new_data_scaled)

        return render_template('home.html', result=result[0])
    else:
        return render_template('home.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
