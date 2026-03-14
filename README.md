# GPS Microservice using Docker, Kubernetes (Minikube) and Prometheus

## Overview
This project demonstrates a cloud-native microservice that shares the GPS location of a classroom. The service is containerized using Docker and deployed on a Kubernetes cluster using Minikube. Prometheus is used to monitor container performance, and a CI/CD pipeline is implemented using GitHub Actions.

## Technologies Used
- Python (Flask)
- Docker
- Kubernetes (Minikube)
- Prometheus
- GitHub Actions (CI/CD)

## Project Tasks

### Task 1: Microservice Deployment
A Python-based microservice was developed using Flask to share GPS location data. The service was containerized using Docker and deployed on the Minikube Kubernetes cluster.

### Task 2: Container Monitoring
Prometheus was deployed to monitor the performance of containers running in the Kubernetes cluster. It collects metrics such as CPU usage, memory consumption, and pod information.

### Task 3: CI/CD Pipeline
A CI/CD pipeline was implemented using GitHub Actions. The workflow automatically builds the Docker image whenever changes are pushed to the repository.

## Files in the Repository
- app.py – Flask microservice code
- Dockerfile – Docker configuration file
- requirements.txt – Python dependencies
- prometheus-deployment.yaml – Prometheus deployment configuration
- prometheus-service.yaml – Prometheus service configuration
- README.md – Project documentation


minikube start


Deploy Prometheus

kubectl apply -f prometheus-deployment.yaml
kubectl apply -f prometheus-service.yaml


Check Pods

kubectl get pods


Access Prometheus Dashboard

minikube service prometheus-service


## Author
N Harsha Vardhan  
Roll No: 2023BCS0158  
Cloud Computing Lab

## Running the Project

Start Minikube
