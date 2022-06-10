# Introduction to MLOps

## Title 
Introduction to MLOps

## Abstract
After successfully training a machine learning model, we need to deploy this model to production. This step is crucial to the success of our product because "No users, no party!".
In this talk, we will introduce how to serve ML models to a large number of users, technologies that facilitate this, and how to glue them together.

## Topics

* Python HTTP Clients - Flask, FastAPI 
* Running HTTP Clients locally 
* Serving ML Models 
* Containerization 
* Kubernetes 
* Kubernetes Deployment

## Requirements
* minikube
* kubectl
* docker

## Installing `minikube`

Installation guide is [here](https://minikube.sigs.k8s.io/docs/start/).

### MacOS
```shell
brew install minikube
```

## Installing `kubectl`

Detailed installation guide [here](https://kubernetes.io/docs/tasks/tools/).

### MacOS
```shell
brew install kubectl
```

## Install `docker`
Install docker for your OS from [here](https://docs.docker.com/get-docker/).
``
## Getting started

### Start local k8s cluster
```shell
minikube start --driver=docker --kubernetes-version=v1.21.6 --mount
```

### Check the installation
Open kubernetes dashboard:
```shell
minikube dashboard
```

### Build Docker image
#### locally
```shell
cd 4_docker
docker build -t hello-ml .
minikube image load hello-ml
```

### Install the application
```shell
cd ../5_kubernetes
kubectl apply -f deployment.yaml
```

### Make application reachable
```shell
kubectl port-forward svc/flask-service 5000:5000
```
At `localhost:5000` you should see the hello message.

### Send request

```shell
curl --request POST 'http://localhost:5000/predict' \
--header 'Content-Type: application/json' \
--data-raw '{
"fixed acidity": 5,
"volatile acidity": 5,
"citric acid":5,
"residual sugar": 5,
"chlorides": 5,
"free sulfur dioxide": 5,
"total sulfur dioxide": 5,
"density": 5,
"pH": 5,
"sulphates": 5,
"alcohol": 5
}'
```
