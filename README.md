# Crypto Exchange Platform

This project is a cryptocurrency exchange platform built with Django. It supports background task processing with Celery and can be run locally or with Docker.

## Features
- Cryptocurrency management (add, update, delete)
- Historical price tracking
- Background tasks with Celery
- RESTful API endpoints
- Dockerized for easy deployment

## Requirements

- Python 3.11+
- pip
- Docker & Docker Compose (optional, for containerized setup)

## Local Setup (Without Docker)

1. **Clone the repository:**
	```bash
	git clone <repo-url>
	cd crypto-exchange
	```

2. **Create a virtual environment and activate it:**
	```bash
	python3 -m venv venv
	source venv/bin/activate
	```

3. **Install dependencies:**
	```bash
	pip install -r requirements.txt
	```

4. **Apply migrations:**
	```bash
	python manage.py migrate
	```

5. **Run the development server:**
	```bash
	python manage.py runserver
	```

6. **Start Celery worker (in a new terminal):**
	```bash
	celery -A crypto worker -l info
	```

7. **(Optional) Start Celery beat for scheduled tasks:**
	```bash
	celery -A crypto beat -l info
	```

## Running with Docker

1. **Build and start the containers:**
	```bash
	docker-compose up --build
	```

2. The app will be available at `http://localhost:80/` (via nginx) when running with Docker.

---

**Note:**
- When running manually (without Docker), the app is available at `http://localhost:8000/`.
- When running with Docker (using nginx), the app is available at `http://localhost:80/`.

## Project Structure

- `crypto/` - Django project settings and configuration
- `currencies/` - App for managing cryptocurrencies
- `requirements.txt` - Python dependencies
- `Dockerfile` & `docker-compose.yml` - Docker configuration

## Useful Commands

- Create superuser:
  ```bash
  python manage.py createsuperuser
  ```
- Access Django admin:
	- `http://localhost:8000/admin/` (manual run)
	- `http://localhost:80/admin/` (Docker/nginx)

## License

MIT License
# crypto-exchange