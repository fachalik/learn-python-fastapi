import os

# Define project structure
folders = [
    "app/api",
    "app/core",
    "app/models",
    "app/schemas",
    "app/services",
    "app/db",
    "app/tests",
    ".github",
    "docs"
]

files = {
    "app/api/v1.py": "# API routes (versioned)",
    "app/api/dependencies.py": "# Common dependencies",
    "app/core/config.py": "# Application settings",
    "app/core/security.py": "# Authentication & security",
    "app/models/user.py": "# Database model (SQLAlchemy)",
    "app/schemas/user.py": "# Pydantic schemas",
    "app/services/user.py": "# Business logic for users",
    "app/db/session.py": "# Database session setup",
    "app/db/init_db.py": "# Initial database setup",
    "app/tests/test_user.py": "# Unit tests",
    "app/main.py": "# Entry point for FastAPI app",
    "app/dependencies.py": "# Shared dependencies",
    "app/logging_config.py": "# Logging setup",
    ".env": "# Environment variables",
    ".gitignore": "venv/\n__pycache__/\n.env",
    "requirements.txt": "fastapi\npydantic\nuvicorn\nsqlalchemy",
    "Dockerfile": "FROM python:3.11\nWORKDIR /app",
    "docker-compose.yml": "# Docker Compose setup",
    "README.md": "# FastAPI Project",
    "pyproject.toml": "# Python project config"
}

# Create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Create files
for file_path, content in files.items():
    with open(file_path, "w") as f:
        f.write(content)

print("✅ FastAPI project structure created!")
