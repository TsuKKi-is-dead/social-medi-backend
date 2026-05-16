from typing import Optional

from fastapi import Body, FastAPI, Response , status,HTTPException
from httpx import post
from pydantic import BaseModel
from random import randrange

app = FastAPI()

class Post(BaseModel): #This is a pydantic model to define schema 
    title: str  #This are the schema for title
    content: str  #We can access the content by calling it
    published:bool = True
    rating:Optional[int] = None #Optional is import from typing 
    #and it means that the rating can be an integer or it can be None,
    # which is the default value if not provided

my_posts = [{"title":"title of post 1","content":"content of post 1","id":1},
            {"title":"title of post 2","content":"content of post 2","id":2}] #We hardcoded the memory for now with each having its unique id   

def find_post(id):
    for post in my_posts:
        if post['id'] == id:
            return post
        
def find_index_post(id):
    for i, post in enumerate(my_posts):
        if post['id'] == id:
            return i

@app.get("/") #This represents the path dir "/":root @:async
async def root():
    return {"message": "Welcome to my API"}

@app.get("/posts")
async def get_post():
    return{"data":my_posts}

@app.get("/comments")
async def get_comments():
    return{"data":"This is your comment"}

@app.post("/posts", status_code=status.HTTP_201_CREATED) #This is to set the status code to 201 when a post is created
async def create_post(post: Post):
    new_post_dict = post.dict() #This is to convert the pydantic model to a dictionary
    new_post_dict['id'] = randrange(0,1000000) #This is to generate a random id for the post
    print(new_post_dict)
    my_posts.append(new_post_dict)
    return{"data":new_post_dict} 

@app.get("/posts/{id}")#we can also use path parameters to get a specific post by its id
async def get_post(id:int, response:Response):#the path parameter is always string and we need to convert it to int
    post = find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id {id} not found")   
    #This above code is another and right way to right a HTTPException instead of using the response object to set the status code and return a message
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return{"message":f"post with id {id} not found"}
    return{"post_detail":post}

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT) #This is to set the status code to 204 when a post is deleted
async def delete_post(id:int):
    index = find_index_post(id)
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id {id} not found")   
    my_posts.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT) #This is to return a response with status code 204 when a post is deleted