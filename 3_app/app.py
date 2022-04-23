import pickle
import numpy as np
import logging
import dill

from flask import Flask, request
from ml_utils import CleanTextTransformer, SpacyTokenTransformer

logging.basicConfig(level=logging.INFO)

model = pickle.load(open('model.pkl', 'rb'))

app = Flask(__name__)


def setup_app(app, models_dir="/models"):
    clean_text_transformer = CleanTextTransformer()
    spacy_tokenizer = SpacyTokenTransformer()

    with open(f"{models_dir}/tfidf_vectorizer.model", "rb") as model_file:
        tfidf_vectorizer = dill.load(model_file)

    with open(f"{models_dir}/lr.model", "rb") as model_file:
        lr_model = dill.load(model_file)


setup_app(app)


@app.route('/')
def hello():
    logging.info(f"Received request.")
    return "Hello"


# https://medium.com/analytics-vidhya/create-your-first-ml-web-app-with-flask-ed0c4bb54312
# Refactor when model file is available
@app.route('/predict', methods=['POST'])
def predict():
    # clean_text = self._clean_text_transformer.transform(X)
    # spacy_tokens = self._spacy_tokenizer.transform(clean_text)
    # tfidf_features = self._tfidf_vectorizer.transform(spacy_tokens)
    # predictions = self._lr_model.predict_proba(tfidf_features)
    features = list(request.json.values())
    logging.info(f"Received json: {features}")

    final_features = [np.array(features)]
    prediction = model.predict(final_features)

    logging.info(f"prediction: {prediction}")

    return {"quality": prediction[0]}
