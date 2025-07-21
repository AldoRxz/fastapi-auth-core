# FastAPI Auth Kit 🔐

A secure, reusable authentication system built with **FastAPI**, designed to be easily integrated into any project.

This starter includes:
- User registration and login
- JWT token authentication
- Password hashing with Bcrypt
- SQLite / PostgreSQL / Supabase support
- Environment-based configuration
- Docker and Docker Compose setup
- Protected routes using JWT

---

## ✨ Features

- Register new users  
- Secure login with JWT tokens  
- Encrypted passwords with `bcrypt`  
- Switchable DB: SQLite (dev), PostgreSQL (prod), or Supabase (cloud)  
- Ready for OAuth integration (Google, GitHub)  
- Docker support  
- Protected routes with JWT

---

## 🗂️ Project Structure


```
fastapi-auth-kit/
│
├── app/
│   ├── api/
│   │   └── routes/
│   │       └── auth.py
│   ├── core/
│   │   └── security.py
│   ├── db/
│   │   ├── models.py
│   │   └── session.py
│   ├── schemas/
│   │   └── user.py
│   └── main.py
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

---


---

## 🚀 Installation (Local)

```bash
# 1. Clone the repository
git clone https://github.com/AldoRxz/fastapi-auth-core.git
cd fastapi-auth-kit

# 2. Create and activate a virtual environment
python -m venv env
.\env\Scripts\activate      # Windows
# source env/bin/activate  # Linux/macOS

# 3. Install dependencies
pip install -r requirements.txt

# 4. Create .env file
cp .env.example .env

# 5. Run the app
uvicorn app.main:app --reload

```

# Build and run containers
docker-compose up --build -d

# To recreate tables (if needed)
docker-compose exec fastapi-app python create_tables.py

---

## API Endpoints

| Method | Path            | Description        |
|--------|-----------------|--------------------|
| POST   | `/auth/register` | Register new user  |
| POST   | `/auth/login`    | Login and get JWT  |
| GET    | `/auth/me`       | Protected route (JWT)  |

All endpoints are available at:

```
http://127.0.0.1:8000/docs
```

---

## Sample `.env` File

### SQLite (dev)
```env
DATABASE_URL=sqlite:///./test.db
SECRET_KEY=mysecretkey
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```
### PostgreSQL local (Docker)
```env
DATABASE_URL=postgresql://postgres:secret123@db:5432/fastapi_db
SECRET_KEY=mysecretkey
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

## To Do (Next Steps)

- [✅] Add protected routes using JWT  
- [ ] Add Google / GitHub OAuth2  
- [ ] Add user email verification  
- [ ] Add Alembic for DB migrations  
- [ ] Package for reuse in multiple apps

---
