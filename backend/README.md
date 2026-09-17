# Manager Data AI

Modular FastAPI MVP for safe data management. It includes agent orchestration, provider abstraction, local fallback, research/cache interfaces, memory, auth, security policy, cost/audit/update interfaces, PostgreSQL/Redis Docker services and migration seed.

## Run locally
`cp .env.example .env && uvicorn app.main:app --reload`

With Docker: `docker compose up --build`.

Endpoints: `GET /health`, `POST /api/v1/auth/token`, `GET /api/v1/auth/me`, `GET /api/v1/agents`, `POST /api/v1/chat` (Bearer token unless `AUTH_DISABLED=true`).

No external provider, email, web search, or unsafe action is enabled by default. Configure and review integrations before enabling them.
