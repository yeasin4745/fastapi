from fastapi import FastAPI

from app.routers import items


app = FastAPI(
    title="My FastAPI Project",
    description="A REST API with CRUD operations",
    version="1.0.0"
)


# Register routers
app.include_router(
    items.router,
    prefix="/api/v1"
)


@app.get("/")
def root():

    return {
        "status": "running",
        "message": "FastAPI server is working"
    }


@app.get("/health")
def health_check():

    return {
        "status": "healthy"
    }
