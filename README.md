# 🚀 NotificationService – CI/CD DevOps Pipeline Project

This project simulates a microservice deployment workflow for a fictional `NotificationService` REST API. The focus is not on application complexity, but on building a complete **DevOps pipeline** using modern industry tools such as **Maven, Jenkins, Docker, Ansible**, and **Grafana monitoring**.

---

## 🧱 Project Structure

```
NotificationService-CICD-DevOps/
├── src/                          # Java Spring Boot source code
│   └── NotificationServiceApplication.java
├── test/                         # Unit test with JUnit
│   └── NotificationServiceApplicationTests.java
├── ansible/                      # Ansible deployment playbook
│   └── deploy-notification.yml
├── docker/                       # Dockerfile for containerization
│   └── Dockerfile
├── metrics/                      # Monitoring scripts
│   ├── send_metric.py
│   └── graphite_test_metric.sh
├── pom.xml                       # Maven build config
└── README.md                     # Project documentation
```

---

## 🔧 Tech Stack

| Tool         | Purpose                        |
|--------------|--------------------------------|
| Java 17 + Maven | Build & Dependency Management |
| Spring Boot  | REST API Framework             |
| JUnit        | Unit Testing                   |
| Docker       | Containerization               |
| Jenkins      | Continuous Integration (CI)    |
| Ansible      | Deployment Automation (CD)     |
| StatsD + Graphite + Grafana | Monitoring & Metrics    |

---

## 🚦 CI/CD Pipeline Overview

1. **Code Build**: Maven compiles & packages the app
2. **Dockerization**: Jenkins builds a Docker image from `Dockerfile`
3. **Deployment**: Ansible playbook stops the running container and deploys a new one
4. **Monitoring**: API sends metrics to StatsD → Graphite → visualized in Grafana

---

## ✅ Setup & Run

### 🧪 Run Tests
```bash
mvn test
```

### 🐳 Build Docker Image
```bash
docker build -t notification-service:1.0 -f docker/Dockerfile .
```

### 🚀 Deploy with Ansible
```bash
ansible-playbook ansible/deploy-notification.yml -i localhost,
```

### 📊 Send Metrics
```bash
python3 metrics/send_metric.py
```

---

## 🎯 Key Learning Outcomes

- End-to-end DevOps pipeline simulation
- Structured repo like a real microservice project
- Setup of full automation from code → container → deployment → monitoring

---

## 🙋‍♂️ Author

**M. Yogeswar Reddy**  
B.Tech CSE, VIT-AP  
[GitHub Profile](https://github.com/yogeswarreddy197)


