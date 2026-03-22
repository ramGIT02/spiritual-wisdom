o	os.getenv (not found)
o	os.environ (not found)

o	BaseSettings
# Backend Environment Variables

## Configuration Pattern

- Uses Pydantic BaseSettings (centralized config)
- No usage of os.getenv or os.environ (good)

## Variables (from Settings)

- APP_NAME
- APP_ENV
- APP_DEBUG
- DATABASE_URL
- CORS_ORIGINS
- OPENAI_API_KEY
- EMBEDDING_MODEL
- CHAT_MODEL
- TOP_K_RETRIEVAL

## Required Variables (Production)

- DATABASE_URL
- OPENAI_API_KEY
- NEXT_PUBLIC_API_BASE_URL

## Optional / Defaults

- APP_ENV (default: development)
- APP_DEBUG (default: true)
- EMBEDDING_MODEL (default: text-embedding-3-small)
- CHAT_MODEL (default: gpt-5-mini)
- TOP_K_RETRIEVAL (default: 6)

## Environment Locations

Backend:
- Local: .env
- Production: Railway Variables

Frontend:
- Local: .env.local
- Production: Vercel Environment Variables

## Observations

- Uses centralized config (good)
- Values loaded via BaseSettings
- No scattered environment variable usage


Check frontend for:
o	process.env
# Frontend Environment Variables

## Used variables

- NEXT_PUBLIC_API_BASE_URL
## Critical Dependency

- NEXT_PUBLIC_API_BASE_URL must point to Railway backend
- Missing value causes frontend API failures

## Where used

- app/page.tsx
- app/concepts/page.tsx
- app/practices/page.tsx
- app/scriptures/page.tsx
- lib/api.ts

## Behavior

- Used as base URL for backend API calls
- Fallback to "http://localhost:8000" if not set

## Observations

- Variable is used consistently across frontend
- Fallback to localhost can cause issues in production if env is missing
- Should ensure NEXT_PUBLIC_API_BASE_URL is always set in Vercel
