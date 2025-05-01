Here’s your complete `README.md` for `dev/bkend/`:

```markdown
# 🐍 Flask Todo App — Local Backend (Dockerized)

This is a simple Flask-based backend app used for local CI/CD testing.

---

## 📁 Folder Location

```
todo-app/dev/bkend/app/
```

---

## ⚙️ Build Instructions

```bash
# Step into the app directory
cd dev/bkend/app

# Build the Docker image with a custom tag
docker build -t flask-todo-app:v1 .
```

---

## 🚀 Run Instructions

```bash
# Map host port 8000 to container port 8000
docker run -d -p 8000:8000 flask-todo-app:v1
```

> ✅ Visit in your browser: [http://localhost:8000](http://localhost:8000)

---

## 🐳 Docker Image Details

| Setting         | Value                       |
|-----------------|-----------------------------|
| Base image      | python:3.10-alpine          |
| App port        | 8000 (inside + host)        |
| Entry point     | `python app.py`             |
| Dependencies    | Flask (`requirements.txt`)  |
| Tag used        | `flask-todo-app:v1`         |

---

## 🧪 Verify Container

```bash
docker ps        # Check running containers
docker logs <id> # View logs if needed
```

---

## 🧼 Cleanup

```bash
docker stop <id>
docker rm <id>
```

---

## ✅ Status

This backend is now ready for:

- 🔧 Jenkins integration
- 🚢 Docker push to registry
- ☸️ K8s deployment via manifests

```

---

## ✅ Next Step: Commit & Push
## After that CI/CD setup under cicd/jenkins
