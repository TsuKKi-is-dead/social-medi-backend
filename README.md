# social-medi-backend

# 📱 Social Media Backend

A backend API for a social media platform — built to learn backend development with FastAPI.

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)

---

## 🚀 About

This is a learning project where I build a social media backend from scratch.
Covering REST APIs, authentication, databases, and everything in between.

---

## 🛠️ Tech Stack

- **Framework** — FastAPI
- **Database** — PostgreSQL + SQLAlchemy
- **Auth** — JWT Authentication
- **Validation** — Pydantic
- **HTTP Client** — HTTPX

---

## 📌 Features (Progress)

- [✅] CRUD Posts
- [ ] User Registration & Login
- [ ] JWT Authentication
- [ ] Like / Unlike Posts
- [ ] Follow / Unfollow Users
- [ ] Comments

---

## ⚙️ Setup & Run

```bash
# Clone the repo
git clone git@github.com:TsuKKi-is-dead/social-medi-backend.git
cd social-medi-backend

# Create and activate venv
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the server
uvicorn main:app --reload
```

---

## 📁 Project Structure

social-medi-backend/
├── main.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md

---

## 📝 License

This project is for learning purposes.

---

_Built by [Mohit Pradhan](https://github.com/TsuKKi-is-dead) — just a boy trying to stay alive and ship good code. 🚀_
