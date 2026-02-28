# 🚀 DevOps Control Panel

A modern web-based DevOps monitoring dashboard built using Flask and deployed on AWS EC2 using Docker.  
This project provides real-time system metrics visualization with a clean UI and production-ready container setup.

---

## Project Overview

The DevOps Control Panel is a lightweight monitoring dashboard that displays real-time:

- CPU Usage
- Memory Usage
- Disk Usage
- Host Information
- Live Metrics using Charts

The application is containerized using Docker and deployed on an AWS EC2 instance.

This project demonstrates:

- Backend development with Flask
- System monitoring using psutil
- Containerization with Docker
- Cloud deployment on AWS EC2
- Production deployment using Gunicorn

---



## 🏗 Architecture

User (Browser)

↓

Public IP (EC2)

↓

Security Group (Port 5000 / 80 Open)
↓

Docker Container
↓

Gunicorn (WSGI Server)
↓
Flask Application
↓
System Metrics (psutil)



### Deployment Stack

- Hosted on AWS EC2
- Dockerized Application
- Gunicorn for production server
- Bootstrap + Chart.js for UI

---

## 🛠 Tech Stack

- Python
- Flask
- psutil
- Gunicorn
- Docker
- AWS EC2
- Linux
- Bootstrap 5
- Chart.js
- Git & GitHub

---

## 🚀 How To Run Locally

### 1️⃣ Clone Repository
https://github.com/liveayushverma-ui/Devops-control-Panel.git
cd devops-control-panel

### 2️⃣ Install Dependencies
pip install -r requirements.txt

### 3️⃣ Run Application
python app.py

Open browser:


http://localhost:5000
---

## 🐳 Run Using Docker

### Build Image
docker build -t control-panel .

### Run Container
docker run -d -p 5000:5000 --restart always --name control control-panel








## ☁️ AWS Deployment

The application is deployed on:

- AWS EC2 Instance
- Ubuntu Linux
- Docker Engine installed
- Security Group configured to allow inbound traffic on port 5000

Deployment Steps:

1. SSH into EC2
2. Clone repository
3. Build Docker image
4. Run container with restart policy
5. Access via Public IP



Application Screenshot



<img width="1215" height="723" alt="image" src="https://github.com/user-attachments/assets/d968ce0d-2409-4240-8661-3b0a9d68d792" />

---

## 🔒 Production Improvements Implemented

- Multi-stage Docker build for smaller image size
- Gunicorn for production WSGI server
- Docker restart policy enabled
- .dockerignore for optimized build context

---

## 🔮 Future Improvements

- Add Docker container monitoring page
- Add container restart functionality
- Implement CI/CD pipeline with GitHub Actions
- Add Nginx reverse proxy
- Add authentication system
- Add Terraform infrastructure automation
- Add Kubernetes deployment



##  Key Learning Outcomes

- Containerizing Python applications
- Debugging Docker build errors
- Deploying applications on AWS EC2
- Managing Linux servers
- Implementing production-grade deployment practices



## CREATER

Ayush Verma  
DevOps Enthusiast | Cloud & Automation Learner
