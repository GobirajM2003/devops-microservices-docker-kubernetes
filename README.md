# 🚀 DevOps Microservices Project (Docker + Kubernetes)

## 📌 Overview

This project is a real-world DevOps microservices application demonstrating containerization, orchestration, and distributed system design using modern DevOps tools.

It consists of a Flask API, Redis database, and a background worker service, integrated using Docker Compose and deployed on Kubernetes (Minikube).

---

## 🏗️ Architecture

            ┌──────────────┐
            │    User      │
            └──────┬───────┘
                   │
                   ▼
          ┌─────────────────┐
          │   Flask API     │
          │ (Service Layer) │
          └──────┬──────────┘
                 │
    ┌────────────┴────────────┐
    ▼                         ▼

┌──────────────┐ ┌────────────────┐
│ Redis │ │ Worker │
│ (Database) │ │ (Background) │
└──────────────┘ └────────────────┘


---

## ⚙️ Tech Stack

- Python (Flask)
- Redis
- Docker
- Docker Compose
- Kubernetes (Minikube)

---

## 📂 Project Structure


project2/
├── api/
│ ├── app.py
│ ├── Dockerfile
│ └── requirements.txt
├── worker/
│ ├── worker.py
│ └── Dockerfile
├── k8s/
│ ├── api-deployment.yaml
│ ├── api-service.yaml
│ ├── redis-deployment.yaml
│ ├── redis-service.yaml
│ └── worker-deployment.yaml
└── docker-compose.yml


---

## 🚀 Run with Docker Compose

```bash
cd project
docker compose up --build

Access:

http://localhost:5001
☸️ Run with Kubernetes (Minikube)
minikube start --driver=docker
eval $(minikube docker-env)

docker build -t api ./api
docker build -t worker ./worker

kubectl apply -f k8s/
kubectl get pods
kubectl get svc

minikube ip

Open:
http://<minikube-ip>:<nodeport>

📊 Features
Microservices architecture
Redis-based state management
Docker containerization
Kubernetes orchestration
Scalable system design
🎯 Learning Outcomes
Docker & Docker Compose
Kubernetes deployments & services
Microservices communication
DevOps workflow understanding
👨‍💻 Author
Gobiraj M
Aspiring DevOps Engineer 🚀
