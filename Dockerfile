#FROM python:3.8.2-slim
#WORKDIR /app
#
## Install python packages
#COPY requirements.txt requirements.txt
#RUN pip install -r requirements.txt
#RUN python -m spacy download en_core_web_sm
#
#COPY ./models/lr.model /models/lr.model
#COPY ./models/tfidf_vectorizer.model /models/tfidf_vectorizer.model
#
## Copy source code
#COPY ./app .
#
## Port for GRPC
#EXPOSE 6000
## Port for REST
#EXPOSE 9000
#
## Define environment variables
#ENV MODEL_NAME RedditClassifier
#ENV SERVICE_TYPE MODEL
#ENV VERSION A
#
## Changing folder to default user
#RUN chown -R 8888 /app
#
#CMD exec seldon-core-microservice $MODEL_NAME --service-type $SERVICE_TYPE

FROM python:3.8.10

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY app.py app.py
# Uncomment when model file is available
COPY model.pkl model.pkl

EXPOSE 5000

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

CMD ["flask", "run"]
