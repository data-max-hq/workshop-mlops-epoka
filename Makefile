all: minikube

minikube:
	minikube start --driver=docker --kubernetes-version=v1.21.6 \
		--mount

