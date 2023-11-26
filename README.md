

# Simple FastAPI & PostgreSQL Webapp

## Overview

This project is a modern web application utilizing FastAPI for the backend API and PostgreSQL for the database. It showcases simplicity of using FastAPI to create RESTful APIs and demonstrates the use of PostgreSQL as a robust and reliable database. The application is containerized using Docker, which ensures consistency across different environments and simplifies deployment processes.

## Features

- **FastAPI Backend**: A high-performance, easy-to-use framework for building APIs with Python 3.7+ based on standard Python type hints.
- **PostgreSQL Database**: A powerful, open-source object-relational database system that uses and extends the SQL language.
- **Docker Integration**: Containerization of both the API and the database for easy deployment and scalability.

## Getting Started

### Prerequisites

- Docker
- Docker Compose
- Python 3.7+ (for local development and testing)

### Installation

1. **Clone the Repository**

   ```bash
   git clone 
   cd https://github.com/AnelMusic/postgress_fastpi_backend_demo
   ```

2. **Build and Run with Docker Compose**

   ```bash
   docker-compose up --build
   ```

   This command builds the Docker images for the API and the database and starts the containers.

### Accessing the Application

- The API will be available at `http://localhost:8000`
- API documentation (auto-generated by FastAPI) can be found at `http://localhost:8000/docs`

## Project Structure

```
myapp/
│
├── api/
│   ├── main.py         # Entry point for the FastAPI application
│   ├── routes.py       # API route definitions
│   ├── schemas.py      # Pydantic schemas for request and response data
│   └── Dockerfile      # Dockerfile for building the API container
│
├── database/
│   ├── Dockerfile.py   # Dockerfile for setting up the PostgreSQL container
│   └── init.sql        # Table creation script
│
├── docker-compose.yml  # Docker Compose configuration
├── requirements.txt    # Dependencies
└── README.md           # Project documentation
```

## Advantages of Containerization

- **Consistent Environment**: Docker ensures that the application runs the same in every environment, from development to production.
- **Isolation**: Dependencies and configurations are encapsulated in containers, reducing conflicts between different projects.
- **Scalability**: Easily scale the application by managing multiple containers.
- **Rapid Deployment**: Containers can be quickly started, stopped, and replicated.

**.env file was comitted on purpose as some users might not be familiar with it
