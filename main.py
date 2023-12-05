from fastapi import FastAPI

from typing import Union, Optional
# Pydantic
from pydantic import BaseModel




# Models Schema
class Post(BaseModel):
    id: Optional[str] = None
    title: str
    content: str
    is_published: bool = False
    rating: Union[int, float] = None


# Initialize app
app = FastAPI()


MY_POSTS = {
    "data": []
}


# Define path operator and function
@app.get("/")
async def hello():
    return {"Post API": "Welcome to my API"}

