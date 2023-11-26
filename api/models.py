# models.py
from pydantic import BaseModel

class UserBase(BaseModel):
    first_name: str
    last_name: str
    age: int
    salary: float  
