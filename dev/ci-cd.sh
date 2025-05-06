#!/bin/bash
set -e

# ------------------------------------------
# 1. CONFIG: Define image and DockerHub details
# ------------------------------------------
IMAGE_NAME=flask-todo-app
IMAGE_TAG=v6.2
DOCKER_IMAGE=yogidockr/$IMAGE_NAME:$IMAGE_TAG

#echo "[STEP 1] Navigate to dev/"
#cd dev || exit 1

# ------------------------------------------
# 2. Build Docker image
# ------------------------------------------
echo "[STEP 2] Building Docker image: $DOCKER_IMAGE"
docker build -t $DOCKER_IMAGE -f Dockerfile .

# ------------------------------------------
# 3. Login to DockerHub
# Jenkins injects DOCKERHUB_USER and DOCKERHUB_PASS as env vars
# ------------------------------------------
echo "[STEP 3] Logging into DockerHub as $DOCKERHUB_USER"
echo "$DOCKERHUB_PASS" | docker login -u "$DOCKERHUB_USER" --password-stdin

# ------------------------------------------
# 4. Push image to DockerHub
# ------------------------------------------
echo "[STEP 4] Pushing image to DockerHub"
docker push $DOCKER_IMAGE

# ------------------------------------------
# 5. Kubernetes Deploy via kubectl
# ------------------------------------------
echo "[STEP 5] Applying K8s deployment & service manifests"
kubectl apply -f k8s/deployment.yml
kubectl apply -f k8s/service.yml

# ------------------------------------------
# 6. Rollout status
# ------------------------------------------
echo "[STEP 6] Waiting for rollout to complete..."
kubectl rollout status deployment/flask-todo-deployment

echo "✅ v6.2 deployed to Minikube. Access it via: minikube service flask-todo-service"
