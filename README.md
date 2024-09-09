# Forest-Fire-Prediction

This project aims to predict the Fire Weather Index (FWI), which estimates the likelihood and intensity of forest fires based on various meteorological factors. The prediction model is built using machine learning techniques and is designed to help forest management authorities and fire departments assess fire risks in a given region.
Project Overview

Forest fires are one of the most dangerous natural disasters, often causing severe damage to the environment, wildlife, and human life. The Fire Weather Index (FWI) is an effective metric to estimate fire danger levels, using inputs such as temperature, humidity, wind speed, and precipitation.

This project includes:

    Data preprocessing: Cleaning and preparing meteorological data.
    Feature engineering: Selecting key variables such as Temperature, Relative Humidity, Wind Speed, etc.
    Machine learning model: Training a model (e.g., Ridge Regression) to predict FWI.
    Web interface: A user-friendly web application built using Flask, where users can input meteorological data to predict fire risk.

Features

    Model: Ridge Regression model with hyperparameter tuning for better prediction accuracy.
    Web Application: Built using Flask to provide easy access to fire risk predictions.
    Input Variables:
        Temperature (°C)
        Relative Humidity (%)
        Wind Speed (km/h)
        Rain (mm)
        Fine Fuel Moisture Code (FFMC)
        Duff Moisture Code (DMC)
        Initial Spread Index (ISI)
        Classes (Fire intensity class)
        Region (Area code)

  How to Run the Project

    Clone the repository:


    git clone https://github.com/svtripathii/Forest-Fire-Prediction.git

    Install dependencies: Navigate to the project folder and install the necessary Python libraries.


    pip install -r requirements.txt

    Run the web application:


    python app.py

    Access the application: Open your browser and navigate to:

    arduino

    http://localhost:5000

Predict FWI: Input meteorological data into the form to get predictions on the fire risk in a particular region.

echnologies Used

    Python: Core programming language.
    Flask: Web framework for creating the web application.
    Scikit-learn: For building the machine learning model.
    Pandas and NumPy: For data manipulation and analysis.
    HTML/CSS: Frontend design of the web interface.

Model Details

    The project uses Ridge Regression to predict FWI, as it handles multicollinearity and prevents overfitting.
    StandardScaler is used to standardize the input features before feeding them into the model.
    The trained model and scaler are saved as .pkl files and loaded in the Flask application to serve real-time predictions.


Project Structure:

├── app.py                # Flask app for prediction
├── models/               # Contains the trained ML model and scaler
├── static/               # CSS, JS, and images
├── templates/            # HTML files for web interface
├── README.md             # Project documentation
└── requirements.txt      # Python dependencies
