# main.py
from fastapi import FastAPI
from routes import user_router

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Welcome! Please go to localhost:8000/docs to see the API documentation."}

app.include_router(user_router, prefix="/users")
