import pickle
import numpy as np
import logging

from flask import Flask, request

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - [%(filename)s:%(lineno)d] - %(levelname)s - %(message)s'
)

model = pickle.load(open('../2_models/model.pkl', 'rb'))

app = Flask(__name__)


@app.route('/')
def hello():
    logging.info(f"Received request.")
    return "Hello"


# https://medium.com/analytics-vidhya/create-your-first-ml-web-app-with-flask-ed0c4bb54312
# Refactor when model file is available
@app.route('/predict', methods=['POST'])
def predict():
    features = list(request.json.values())
    logging.info(f"Received json: {features}")

    final_features = [np.array(features)]
    prediction = model.predict(final_features)[0]

    logging.info(f"prediction: {prediction}")

    response = {
        "prediction": prediction
    }

    return response


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
