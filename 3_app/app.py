import logging
import pickle
import os

from flask import Flask, request

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - [%(filename)s:%(lineno)d] - %(levelname)s - %(message)s'
)

app = Flask(__name__)
clean_text_transformer = CleanTextTransformer()
spacy_tokenizer = SpacyTokenTransformer()

models_dir = os.environ["MODELS_DIR"]


def load_model():
    with open(f"{models_dir}/model.pkl", "rb") as model_file:
        model = pickle.load(model_file)
    return model


model = load_model()


@app.route('/')
def hello():
    logging.info(f"Received request.")
    return "Hello"


@app.route('/predict', methods=['POST'])
def predict():
    """
    Do prediction
    :return: json with prediction
    """
    payload = request.json
    logging.info(f"Payload: {payload}")
    prediction = model.predict(payload)

    logging.info(f"prediction: {predictions}")
    sentiment = predictions[0]
    logging.info(f"sentiment: {sentiment}")
    sentiment_json = {
        "positive": sentiment[0],
        "negative": sentiment[1]
    }

    return sentiment_json


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5005)
