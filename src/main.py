from fastapi import FastAPI
from src.routes.books import router as book_router

app = FastAPI()

# Include Book Routes
app.include_router(book_router)

@app.get("/")
def home():
    return {"message": "FastAPI + PostgreSQL CRUD API is running!"}
