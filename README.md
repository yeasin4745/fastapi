## FastAPI CRUD API

A modular REST API built with Python, FastAPI, and Uvicorn, featuring CRUD operations and Pydantic validation.

Tech Stack

- Python
- FastAPI
- Uvicorn
- Pydantic
- uv

Project Structure

src/app/
├── main.py
├── routers/
│   └── items.py
├── schemas/
│   └── item.py
└── services/
    └── item_service.py

## Installation & Run

** Clone repository **
`git clone https://github.com/yeasin4745/fastapi.git`
`cd fastapi`

# Install dependencies
`pip install uv`
`uv sync`

# Start development server
```uv run uvicorn app.main:app --reload```

Server: "http://127.0.0.1:8000"

API Documentation: "/docs"

API Endpoints

Base URL: "/api/v1"

Method| Endpoint| Description
GET| "/"| Root
GET| "/health"| Health check
POST| "/items/"| Create item
GET| "/items/"| Get all items
GET| "/items/{item_id}"| Get item
PUT| "/items/{item_id}"| Update item
DELETE| "/items/{item_id}"| Delete item

Request Example
```
{
  "name": "Keyboard",
  "description": "Mechanical Keyboard",
  "price": 2500,
  "in_stock": true
}
```
# Architecture

- Main: Application initialization and router registration.
- Routers: API endpoints.
- Schemas: Pydantic validation.
- Services: Business logic and CRUD operations.

Storage

Currently uses Python Dictionary-based in-memory storage. Data is lost when the server restarts.

Roadmap

- [x] Project structure refactoring
- [x] REST API endpoints
- [x] CRUD operations
- [x] Pydantic validation
- [ ] SQLite / PostgreSQL
- [ ] PATCH endpoint
- [ ] Authentication & Authorization
- [ ] Automated testing
- [ ] Request logging

