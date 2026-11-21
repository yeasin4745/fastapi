FastAPI CRUD API

A structured REST API built with Python, FastAPI, and Uvicorn. This project demonstrates modular project architecture, API endpoint development, Pydantic validation, and CRUD operations.

Project Overview

This project is designed to build a modular REST API using FastAPI.

Key Features

- Modular project structure
- RESTful API endpoints
- CRUD operations (Create, Read, Update, Delete)
- Request validation using Pydantic
- HTTP status code handling
- Error handling with HTTPException
- Interactive API documentation using Swagger UI

Technology Stack

Technology| Purpose
Python| Programming Language
FastAPI| API Framework
Uvicorn| ASGI Server
Pydantic| Data Validation
uv| Package and Project Management

Project Structure

fastapi/
│
├── src/
│   └── app/
│       ├── __init__.py
│       ├── main.py
│       │
│       ├── routers/
│       │   ├── __init__.py
│       │   └── items.py
│       │
│       ├── schemas/
│       │   ├── __init__.py
│       │   └── item.py
│       │
│       └── services/
│           ├── __init__.py
│           └── item_service.py
│
├── pyproject.toml
├── uv.lock
├── README.md
└── .gitignore

Installation

1. Clone the Repository

git clone <YOUR_REPOSITORY_URL>

2. Enter the Project Directory

cd fastapi

3. Install Dependencies

Install uv if it is not already installed:

pip install uv

Synchronize the project environment:

uv sync

Run the Application

Start the development server:

uv run uvicorn app.main:app --reload

The server will be available at:

http://127.0.0.1:8000

API Documentation

Swagger UI:

http://127.0.0.1:8000/docs

ReDoc:

http://127.0.0.1:8000/redoc

API Endpoints

Base URL:

/api/v1

Method| Endpoint| Description
GET| "/"| Root endpoint
GET| "/health"| Health check
POST| "/items/"| Create a new item
GET| "/items/"| Retrieve all items
GET| "/items/{item_id}"| Retrieve a specific item
PUT| "/items/{item_id}"| Update an existing item
DELETE| "/items/{item_id}"| Delete an item

CRUD Operations

1. Create Item

Method: "POST"

/api/v1/items/

Request Body:

{
    "name": "Keyboard",
    "description": "Mechanical Keyboard",
    "price": 2500,
    "in_stock": true
}

Successful Response:

{
    "id": 1,
    "name": "Keyboard",
    "description": "Mechanical Keyboard",
    "price": 2500,
    "in_stock": true
}

Status Code: "201 Created"

2. Retrieve All Items

Method: "GET"

/api/v1/items/

3. Retrieve a Specific Item

Method: "GET"

/api/v1/items/1

4. Update Item

Method: "PUT"

/api/v1/items/1

Request Body:

{
    "name": "Gaming Keyboard",
    "description": "RGB Mechanical Keyboard",
    "price": 3500,
    "in_stock": true
}

5. Delete Item

Method: "DELETE"

/api/v1/items/1

Successful Status Code:

"204 No Content"

Request Validation

Pydantic models are used to validate incoming request data.

Example:

price: float = Field(gt=0)

This ensures that the price must be greater than zero.

Other validation rules include:

- Item name must contain at least 2 characters.
- Maximum item name length is 100 characters.
- Price must be positive.
- Stock availability must be a Boolean value.

Invalid request data produces a "422 Unprocessable Entity" response.

Error Handling

The API uses FastAPI's "HTTPException" for handling errors.

Example:

raise HTTPException(
    status_code=404,
    detail="Item not found"
)

Common HTTP status codes:

Status Code| Meaning
200| OK
201| Created
204| No Content
404| Not Found
422| Validation Error

Application Architecture

The project follows a modular architecture based on separation of concerns.

Main Module

"main.py"

Responsible for initializing the FastAPI application and registering routers.

Router Layer

"routers/items.py"

Responsible for defining HTTP endpoints and handling incoming API requests.

Schema Layer

"schemas/item.py"

Responsible for request and response data validation using Pydantic.

Service Layer

"services/item_service.py"

Responsible for implementing business logic and CRUD operations.

Data Storage

Currently, the application uses Python Dictionary-based in-memory storage.

items = {}

Important: Data is temporary and will be lost when the application restarts.

Database integration is planned for a future version.

Development Roadmap

- [x] Project structure refactoring
- [x] REST API endpoint development
- [x] CRUD operations
- [x] Pydantic request validation
- [x] Basic error handling
- [ ] SQLite database integration
- [ ] PostgreSQL support
- [ ] PATCH endpoint
- [ ] Repository Pattern
- [ ] Authentication and Authorization
- [ ] Automated testing with pytest
- [ ] Request logging
- [ ] Production deployment

Learning Objectives

Through this project, the following concepts are explored:

1. FastAPI application architecture.
2. ASGI server fundamentals.
3. REST API design principles.
4. HTTP methods and status codes.
5. Pydantic data validation.
6. Modular Python development.
7. CRUD implementation.
8. Separation of concerns.

License

This project is intended for educational and development purposes.
