from pydantic import BaseModel

class UserCreate(BaseModel):
    first_name: str
    last_name: str
    age: int
    salary: float

class User(UserCreate):
    id: int  # Include the id for responses where the user's id is known

    class Config:
        orm_mode = True
