from pydantic import BaseModel

class Category(BaseModel):
    title: str
    director: str

class Movie(BaseModel):
    id: int
