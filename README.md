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
