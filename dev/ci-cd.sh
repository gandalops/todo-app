#!/bin/bash
set -e

# -------------------------------
# CONFIG
# -------------------------------
IMAGE_NAME=flask-todo-app
IMAGE_TAG=${1:-v6.3}
GIT_HASH=$(git rev-parse --short HEAD)
DOCKER_IMAGE=yogidockr/$IMAGE_NAME:${IMAGE_TAG}-${GIT_HASH}
SONAR_PROJECT_KEY="flask-todo-app"
SONAR_HOST_URL="http://localhost:9000"
SONAR_TOKEN="${SONAR_TOKEN:-your_token_here}"

cd "$(dirname "$0")"

# -------------------------------
# STEP 1: Checkout (implicit via Jenkins/git)
# -------------------------------
echo "[STEP 1] Confirming Git checkout"
git status

# -------------------------------
# STEP 2: Unit Tests
# -------------------------------
# Activate virtual environment
source ~/work/git-repos/todo-app/venv/bin/activate
echo "[STEP 2] Running unit tests"
pytest dev/test/

# -------------------------------
# STEP 3: Code Coverage
# -------------------------------
echo "[STEP 3] Running pytest with coverage"
pytest --cov=dev --cov-report=xml

# -------------------------------
# STEP 4: Software Composition Analysis (SCA)
# -------------------------------
echo "[STEP 4] Running OWASP Dependency Check"
dependency-check.sh --project "$IMAGE_NAME" --scan dev --format XML

# -------------------------------
# STEP 5: Static Application Security Testing (SAST)
# -------------------------------
echo "[STEP 5] Running SonarQube SAST scan"
sonar-scanner \
  -Dsonar.projectKey=$SONAR_PROJECT_KEY \
  -Dsonar.sources=dev \
  -Dsonar.host.url=$SONAR_HOST_URL \
  -Dsonar.login=$SONAR_TOKEN \
  -Dsonar.python.coverage.reportPaths=coverage.xml

# -------------------------------
# STEP 6: Quality Gates (wait via webhook or API polling)
# -------------------------------
echo "[STEP 6] Waiting for SonarQube Quality Gate (simulate delay)"
sleep 10  # Replace with real webhook wait or API polling

# -------------------------------
# STEP 7: Build Docker Image
# -------------------------------
echo "[STEP 7] Building Docker image: $DOCKER_IMAGE"
docker build -t $DOCKER_IMAGE -f Dockerfile . \
  --label git-commit=$GIT_HASH

# -------------------------------
# STEP 8: Image Scanning
# -------------------------------
echo "[STEP 8] Scanning Docker image with Trivy"
trivy image --severity CRITICAL,HIGH $DOCKER_IMAGE

# -------------------------------
# STEP 9: Push to DockerHub
# -------------------------------
echo "[STEP 9] Logging into DockerHub"
echo "$DOCKERHUB_PASS" | docker login -u "$DOCKERHUB_USER" --password-stdin

echo "[STEP 10] Pushing image to DockerHub"
docker push $DOCKER_IMAGE

# -------------------------------
# STEP 11: Kubernetes Deployment
# -------------------------------
echo "[STEP 11] Deploying to Kubernetes"
kubectl apply -f k8s/deployment.yml
kubectl apply -f k8s/service.yml

# -------------------------------
# STEP 12: Rollout Status
# -------------------------------
echo "[STEP 12] Waiting for rollout"
kubectl rollout status deployment/flask-todo-deployment

# -------------------------------
# STEP 13: Smoke Testing
# -------------------------------
echo "[STEP 13] Smoke Testing"
URL=$(minikube service flask-todo-service --url)
echo "Service URL: $URL"
curl --fail "$URL/meta" || (echo "Smoke test failed!" && exit 1)

echo "✅ CI/CD pipeline completed successfully!"
