# Layer 1 Architecture Backend


user request 
  |
api service -> microservice1 
|
redis cache 
|
worker service -> microservice2
|
database

| Component          | Purpose                           |
| ------------------ | --------------------------------- |
| **User**           | Sends request from browser/mobile |
| **API Service**    | Handles HTTP request              |
| **Redis Cache**    | Fast memory storage               |
| **Worker Service** | Background processing             |
| **Database**       | Permanent data storage            |



2️⃣ DevOps Infrastructure View

This is how a DevOps engineer usually sees the system.

                Internet
                    |
                Load Balancer
                    |
             Kubernetes Service
                    |
                API Pods
                    |
               Redis Cache
                    |
               Message Queue
                    |
              Worker Pods
                    |
                Database


| Component          | DevOps Responsibility  |
| ------------------ | ---------------------- |
| Load Balancer      | Traffic distribution   |
| Kubernetes Service | Internal networking    |
| API Pods           | Application containers |
| Redis              | Cache layer            |
| Worker Pods        | Background jobs        |
| Database           | Persistent storage     |


4️⃣ Full Backend Tech Stack

Users
  |
  v
Load Balancer
  |
  v
API Gateway
  |
  v
Microservice 1 (API)
  |
  v
Redis Cache
  |
  v
Message Queue
  |
  v
Worker Microservice
  |
  v
Database

5.Technology Mapping

| Layer         | Example Tools           |
| ------------- | ----------------------- |
| API           | Python / Node / Go      |
| Cache         | Redis                   |
| Queue         | RabbitMQ / Apache Kafka |
| Worker        | Background microservice |
| Database      | PostgreSQL              |
| Container     | Docker                  |
| Orchestration | Kubernetes              |




Project folder structure:
    
Project 
- api 
  app.py 
  dockerfile 
- worker
    worker.py
    dockerfile
- docker-compose.yml
- requirements.txt
