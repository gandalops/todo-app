# todo-app

A small Todo app built with Flask, Docker, Jenkins and Minikube, created in 2025 to practise a local CI/CD workflow.

## Project status

Archived. I built this in 2025 as a hands-on DevOps exercise and stopped working on it after version 6.2. It is kept as a small demonstration.

## How it was built

Commits come from two GitHub accounts on purpose. A second account acted as the developer pushing code, and this account acted as the central repository where I reviewed and accepted changes, to practise a team workflow.

## Tech stack

| Layer | Technology |
| --- | --- |
| Backend | Python (Flask) |
| Database | SQLite (from v6.1) |
| Frontend | HTML, CSS |
| Containerization | Docker |
| Registry | DockerHub |
| CI/CD | Jenkins (dev/ci-cd.sh) |
| Orchestration | Kubernetes on Minikube |

## Run locally

From the dev folder.

Without Docker:

    cd dev
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    python app.py

With Docker:

    cd dev
    docker build -t flask-todo-app:v6.2 .
    docker run -p 8000:8000 flask-todo-app:v6.2

Then open http://localhost:8000

## CI/CD

Jenkins runs dev/ci-cd.sh. The script builds the image, pushes it to DockerHub (credentials come from Jenkins as environment variables), applies the manifests in dev/k8s and waits for the rollout on Minikube.

## Security notes

- Flask debug mode was switched off after a review of the code (November 2026).
- No credentials are stored in the repository.
- Known gaps: the container runs as root, there is no image or dependency scanning in the pipeline, and there are no automated tests.

© 2025 Yogesh Shankar Gandal 

