from fastapi import FastAPI
from pydantic import BaseModel
from pydantic_settings import BaseSettings

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    email: str
    age: int

@app.post("/users/")
async def create_user(user: User):
    return "Ok, I have received the user name"+user.name

class Settings(BaseSettings):
    app_name: str
    admin_email: str
    items_per_user: int=50

setting = Settings("Fast api Lesson", "admin@gmail.com" )

@app.get("/users/")
async def create_user():
    return "Elena"