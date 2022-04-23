import pickle
import numpy as np
import logging
import dill

from flask import Flask, request
from ml_utils import CleanTextTransformer, SpacyTokenTransformer

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - [%(filename)s:%(lineno)d] - %(levelname)s - %(message)s'
)

app = Flask(__name__)
clean_text_transformer = CleanTextTransformer()
spacy_tokenizer = SpacyTokenTransformer()


def setup_app(models_dir="/models"):
    with open(f"{models_dir}/tfidf_vectorizer.model", "rb") as model_file:
        tfidf_vectorizer = dill.load(model_file)

    with open(f"{models_dir}/lr.model", "rb") as model_file:
        lr_model = dill.load(model_file)

    return tfidf_vectorizer, lr_model


tfidf_vectorizer, lr_model = setup_app(models_dir="../2_models")


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
    text_array = payload["text"]
    clean_text = clean_text_transformer.transform(text_array)
    spacy_tokens = spacy_tokenizer.transform(clean_text)
    tfidf_features = tfidf_vectorizer.transform(spacy_tokens)
    predictions = lr_model.predict_proba(tfidf_features)

    logging.info(f"prediction: {predictions}")
    sentiment = predictions[0]
    sentiment_json = {
        "positive": sentiment[0],
        "negative": sentiment[1]
    }

    return sentiment_json


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5005)
