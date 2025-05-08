A simple yet evolving Todo app built with Flask, Docker, and Kubernetes, integrated into a Jenkins CI/CD pipeline. This project demonstrates step-by-step implementation of modern DevOps practices in a local development environment.

## 🚀 Project Status

This project is **actively evolving** through multiple versions.  
Stay tuned for future releases with improved architecture, security, observability, and deployment strategies.

## 🧰 Tech Stack

| Layer           | Technology          |
|-----------------|---------------------|
| Backend         | Python (Flask)      |
| Frontend        | HTML, CSS           |
| Containerization| Docker              |
| CI/CD Pipeline  | Jenkins             |
| Orchestration   | Minikube (K8s)      |
| Infra as Code   | Terraform (planned) |



## ⚙️ Local Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/<your-username>/<repo-name>.git
   cd <repo-name>
````

2. **Run Locally Without Docker**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install flask
   python app.py
   ```

3. **Run with Docker**

   ```bash
   docker build -t flask-todo-app:v5 .
   docker run -p 8000:8000 flask-todo-app:v5        #flask default port is 5000
   ```

4. **Deploy via Jenkins CI/CD to Minikube**

   * Make sure Jenkins is set up with Docker and kubectl access.
   * Use the included `Jenkinsfile` to automate build and deploy stages.

## 📌 Version History

### ✅ v1 – Basic Flask App

* Minimal `app.py` using Flask.
* Single route with in-memory list for todos.
* No frontend templates.

### ✅ v2 – UI Enhancement with HTML

* Added `index.html` and basic form.
* Enabled todo addition via browser.
* Used Flask's `render_template`.

### ✅ v3 – Dockerized the App

* Added `Dockerfile`.
* Built and ran the container locally.
* Verified isolated deployment.

### ✅ v4 – Jenkins CI Integration

* Wrote `Jenkinsfile` with CI stages:

  * Git clone
  * Docker build + tag
  * Push to local Docker registry
* Started Minikube-based deployment testing.

### ✅ v5 – Frontend Separation & Volume Mount

* Separated frontend into `templates/` and `static/` folders.
* Used `docker-compose` with volume mount for live dev.
* Added `kubectl set image` for automated rollout in Jenkins.
* Cleaned up old pods/images post-deployment.

## 🔮 What's Next?

Upcoming versions will include:

* Backend database integration (e.g., SQLite or PostgreSQL)
* CI/CD enhancements (e.g., test automation, Trivy scans)
* Helm chart for production-ready Kubernetes deployments
* Secrets management and monitoring integration
* Cloud deployment on AWS/GCP with best practices
* Infrastructure as Code using Terraform

## 🤝 Contributions & Feedback

This project is for educational and portfolio purposes. Feedback and suggestions are welcome!

© 2025 Yogesh Shankar Gandal | DevSecOps Engineer

