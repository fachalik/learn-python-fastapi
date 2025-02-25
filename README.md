# FastAPI User Management

A FastAPI-based user management system with authentication and CRUD operations.

## Features

- ✅ User authentication with JWT
- ✅ CRUD operations for users
- ✅ Database integration with PostgreSQL & Tortoise-ORM
- ✅ API documentation with Swagger & ReDoc
- ✅ Docker support for easy deployment

## Tech Stack

- **FastAPI** - High-performance web framework for APIs
- **PostgreSQL** - Relational database management system
- **Tortoise-ORM** - An easy-to-use async ORM
- **Aerich** - Database migrations for Tortoise-ORM
- **Docker** - Containerization for deployment
- **Uvicorn** - ASGI server for FastAPI
- **Passlib** - Password hashing utility

## Installation

### Prerequisites

- Python 3.11+
- PostgreSQL installed and running
- Docker (optional)

### Setup Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/fastapi-app.git
   ```
2. Navigate to the project folder:
   ```bash
   cd fastapi-app
   ```
3. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
4. Activate the virtual environment:
   - Linux/macOS:
     ```bash
     source venv/bin/activate
     ```
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
5. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
6. Set up environment variables in `.env`
7. Run database migrations:
   ```bash
   aerich upgrade
   ```
8. Start the FastAPI server:
   ```bash
   uvicorn app.main:app --reload
   ```

## API Endpoints

| Endpoint      | Method | Description                            |
| ------------- | ------ | -------------------------------------- |
| `/auth/login` | POST   | Authenticate user and return JWT token |
| `/users/`     | GET    | Get a list of users                    |
| `/users/{id}` | GET    | Get user by ID                         |
| `/users/`     | POST   | Create a new user                      |
| `/users/{id}` | PUT    | Update user by ID                      |
| `/users/{id}` | DELETE | Delete user by ID                      |

## Usage

- **Swagger UI**: Visit [`http://127.0.0.1:8000/docs`](http://127.0.0.1:8000/docs) for interactive API documentation.
- **ReDoc**: Visit [`http://127.0.0.1:8000/redoc`](http://127.0.0.1:8000/redoc) for alternative API documentation.
- **cURL Example**:
  ```bash
  curl -X POST http://127.0.0.1:8000/auth/login -d '{"username": "user", "password": "pass"}'
  ```

## Contributing

Feel free to fork this repo, make your changes, and submit a PR.

## License

This project is licensed under the **MIT License**.
