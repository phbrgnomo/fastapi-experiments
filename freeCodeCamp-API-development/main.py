from random import randrange
from typing import Optional
from fastapi import FastAPI
from httpx import post
from pydantic import BaseModel

# Start a fastapi instance
app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True # Default the value to True
    rating: Optional[int] = None # Optional Value

my_posts = [{"title": "Title 1", "content": "Content 1", "id": 1}, 
            {"title": "Title 2", "content": "Content 2", "id": 2}]

# Define a root route
@app.get("/")
async def root():
    return {"message": "Hello World"}  # Fastapi converts python dict to json

@app.get("/posts")
async def all_posts():
    return my_posts

@app.get("/posts/{id}")
async def get_posts(id: int):
    return next(
        ({"data": p} for p in my_posts if p["id"] == id),
        {"error": "Post not found"},
    )

@app.post("/posts")
async def create_post(post: Post):
    print(post)
    print(post.model_dump()) # Convert pydantic model to a dict
    
    post_dict = post.model_dump()
    post_dict["id"] = randrange(0, 1000000)
    my_posts.append(post_dict)
    
    return {"data": post_dict}
