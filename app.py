"""
This file runs the Flask application we are using as an API endpoint.
"""

import pickle
from math import log10
from flask import Flask
from flask import request
from flask import jsonify
from sklearn import linear_model
from sklearn.externals import joblib
from sklearn import preprocessing

# Create a flask
app = Flask(__name__)

# Load pickled model file
model = joblib.load('chrunlog_r.pk')

# Create an API end point
@app.route('/api/v1.0/predict', methods=['GET'])
def get_prediction(trained_model=model):
    #  ['tenure', 'age', 'address', 'income', 'ed', 'employ', 'equip'] 
    # tenure
    tenure = float(request.args.get('tenure'))
    # age
    age = float(request.args.get('age'))
    # address
    address = float(request.args.get('address'))
    #income
    income = float(request.args.get('income'))
	#ed
    ed = float(request.args.get('ed'))
	#employ
    employ = float(request.args.get('employ'))
	#equip
    equip = float(request.args.get('equip'))
    # The features of the observation to predict
    features =  [tenure, age, address, income, ed, employ, equip] 
    features = preprocessing.StandardScaler().fit(features).transform(features)
    # Predict the class using the model
    predicted_class = int(trained_model.predict([features]))

    # Return a json object containing the features and prediction
    return jsonify(features=features, predicted_class=predicted_class)

if __name__ == '__main__':
    # Run the app at 0.0.0.0:3333
    app.run(port=3333,host='0.0.0.0')