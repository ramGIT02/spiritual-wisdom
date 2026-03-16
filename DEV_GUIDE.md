# Spiritual Wisdom Platform – Developer Guide

## Project Overview

Spiritual Wisdom Platform is a web application for exploring:
- Hindu scriptures
- spiritual concepts
- meditation practices
- grounded spiritual Q&A

## Tech Stack

### Backend
- FastAPI
- SQLAlchemy
- Alembic
- PostgreSQL
- pgvector
- OpenAI API

### Frontend
- Next.js
- React
- TypeScript

### Local Infrastructure
- Docker Desktop
- PostgreSQL container with pgvector

### Planned Production
- Database: Neon
- Backend: Railway
- Frontend: Vercel

---

## Project Structure

```text
spiritual-wisdom/
├── backend/
│   ├── app/
│   ├── alembic/
│   ├── requirements.txt
│   ├── .env
│   ├── .env.example
│   ├── docker-compose.yml
│   └── Dockerfile
├── frontend/
│   ├── app/
│   ├── lib/
│   ├── package.json
│   └── .env.local
├── .gitignore
├── backlog.md
└── DEV_GUIDE.md