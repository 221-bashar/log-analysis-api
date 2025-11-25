# 🔐 Log Analysis API & Dashboard

## Overview

This project is a full-stack, containerized solution designed to parse system logs, detect suspicious security events, and display the results on a simple web dashboard. It demonstrates proficiency in Python OOP, REST API development with Flask, front-end integration using JavaScript, and modern DevOps practices (Docker).

## 🛠️ Tech Stack & Skills

| Category | Technology/Skill | Key Features Demonstrated |
| :--- | :--- | :--- |
| **Backend** | Python, OOP, Regex, JSON | Log Parsing (Structured Data Extraction), Multi-Rule Detection (Failed Login, Path Traversal), Modular Design. |
| **API** | Flask, RESTful Design, CORS | Exposing data via two simple GET endpoints (`/api/logs` and `/api/alerts`). |
| **Frontend** | HTML, CSS, JavaScript (Fetch) | Asynchronous data fetching (`fetch API`), dynamic table rendering, UI integration. |
| **DevOps** | Docker, Git | Containerization for cross-platform stability, port mapping, professional build process. |

## 📐 Project Structure

The architecture is modular, ensuring high cohesion and low coupling between components.

log-analysis-api/ ├── api/ # Flask API, runs detection/ and parser/ │ ├── app.py │ ├── detection/ # Logic for identifying alerts │ └── parser/ # Logic for structuring raw logs ├── frontend/ # HTML/JS dashboard ├── logs/ # Sample logs (auth.log) ├── Dockerfile # Instructions for building the container └── requirements.txt # Python dependency list


## 🚀 How to Run (Docker Deployment)

The easiest way to run the entire system is using Docker, which eliminates environment setup issues.

1.  **Prerequisites:** Ensure **Docker Desktop** is running and **WSL integration** is enabled.
2.  **Build the Image:** Navigate to the project root and build the container image.
    ```bash
    docker build -t log-analysis-api .
    ```
3.  **Run the Container:** Launch the container and map the internal port 5000 to external port 8080.
    ```bash
    docker run -d -p 8080:5000 --name log-analyzer log-analysis-api
    ```
4.  **Access the Dashboard:** Open the `frontend/index.html` file in your web browser. The JavaScript will automatically fetch data from `http://localhost:8080/api/alerts`.

---