# FastAPI Project Setup Guide

## 1. Python Version

* Recommended Python: 3.11.x (>=3.10)

```bash
python --version
```

## 2. Create `requirements.txt`

Include the following dependencies:

```txt
fastapi==0.115.0
uvicorn==0.30.1
sqlalchemy==2.0.34
psycopg2-binary==2.9.9
alembic==1.13.1
python-dotenv==1.0.1
passlib[bcrypt]==1.7.4
python-jose==3.3.0
pytest==8.4.2
requests==2.32.0
```

## 3. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

## 4. Run FastAPI App

* Start Uvicorn server to run your FastAPI app:

```bash
uvicorn app.main:app --reload
```

* Access the API at: [http://127.0.0.1:8000](http://127.0.0.1:8000)  
* API documentation (Swagger UI) at: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)


## 5. Run Tests

```bash
PYTHONPATH=./ python -m pytest -v
```

## 6. Folder Structure

```
project-root/
│
├─ app/
│  ├─ main.py          # FastAPI entrypoint
│  ├─ api/             # API routers
│  │  └─ v1/endpoints/ # Endpoints
│  ├─ models/          # SQLAlchemy models
│  ├─ schemas/         # Pydantic schemas
│  ├─ services/        # Business logic
│  ├─ crud/            # CRUD operations
│  ├─ core/            # DB, config, security, logger
│  └─ utils/           # Helper functions
│
├─ tests/              # Test cases
├─ requirements.txt    # Python dependencies
├─ README.md           # Project readme
└─ Dockerfile/docker-compose.yml (optional)
```

## 7. Notes

* Use `python-dotenv` to load environment variables.
* `uvicorn --reload` allows auto-reloading during development.
* Use `pytest` with `PYTHONPATH=./` to ensure modules inside `app/` are importable.
* For DB migrations, configure `alembic` properly.
* Use `python-jose` for JWT handling.
* `passlib[bcrypt]` for password hashing.
