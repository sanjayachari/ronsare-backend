ronsare-core/
├─ app/
│  ├─ main.py                  # Entry point of FastAPI app
│  ├─ api/
│  │  └─ v1/
│  │     └─ endpoints/
│  │        └─ user.py         # API routes for user-related operations
│  ├─ core/
│  │  ├─ config.py             # Configuration settings (env variables)
│  │  ├─ db.py                 # Database connection setup
│  │  ├─ logger.py             # Logger setup
│  │  └─ security.py           # Security helpers (JWT, password hashing)
│  ├─ crud/
│  │  └─ user.py               # CRUD operations for users
│  ├─ models/
│  │  └─ user.py               # SQLAlchemy ORM models
│  ├─ schemas/
│  │  └─ user.py               # Pydantic schemas for request/response
│  └─ services/
│     └─ user_service.py       # Business logic for users (optional layer)
├─ tests/
│  └─ test_user.py             # Unit tests for user endpoints
├─ docs/
│  ├─ README.md                # Detailed project instructions and Docker guide
│  └─ DOCUMENT.md              # Folder structure & explanation (this file)
├─ Dockerfile                  # Docker image build instructions
├─ docker-compose.yml          # Docker Compose for multi-container setup
├─ requirements.txt            # Python dependencies
├─ alembic.ini                 # Alembic DB migration config
└─ venv/                       # Virtual environment (excluded from Git)
