from fastapi import APIRouter, HTTPException
import psycopg2
import os
from models import UserBase
from tenacity import retry, stop_after_attempt, wait_fixed
from schemas import UserCreate, User  # Import schemas

user_router = APIRouter()


# retry mechanism since docker doesnt guarantee that service is 
# up
@retry(stop=stop_after_attempt(5), wait=wait_fixed(2))
def get_database_connection():
    return psycopg2.connect(
        host="database",
        database="myappdb",
        user=os.environ["POSTGRES_USER"],
        password=os.environ["POSTGRES_PASSWORD"]
    )

# Database connection
conn = get_database_connection()


@user_router.post("/user", response_model=UserBase)
async def add_user(user: UserCreate):
    cur = conn.cursor()
    try:
        cur.execute("INSERT INTO users (first_name, last_name, age, salary) VALUES (%s, %s, %s, %s)",
            (user.first_name, user.last_name, user.age, user.salary))
        conn.commit()
        return user
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))

@user_router.delete("/user/{user_id}")
async def remove_user(user_id: int):
    cur = conn.cursor()
    try:
        cur.execute("DELETE FROM users WHERE id = %s", (user_id,))
        conn.commit()
        return {"message": "User removed successfully"}
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    
@user_router.get("/users")
async def list_users():
    cur = conn.cursor()
    try:
        cur.execute("SELECT * FROM users")
        users = cur.fetchall()
        return users
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
