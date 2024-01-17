from fastapi import FastAPI

app = FastAPI()


@app.get("/") # root route (localhost/)
async def root():
    return {"message": "Hello World"}


@app.get("/items/{item_id}") # items rout (localhost/items/{item_id)}
async def read_item(item_id: int): # require the route value to be an integer, and convert it
    return {"item_id": item_id}

# Because path operations are evaluated in order, you need to make sure that the path 
# for /users/me is declared before the one for /users/{user_id}
# Otherwise, the path for /users/{user_id} would match also for /users/me, 
# "thinking" that it's receiving a parameter user_id with a value of "me".
@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}

@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}

# https://docs.python.org/3/library/enum.html
# The line `from enum import Enum` is importing the `Enum` class from the `enum` module in
# Python's standard library.
from enum import Enum

# Creates a Enum object
class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

@app.get("/models/{model_name}")
# Path parameter with the Enum object annotation
async def get_model(model_name: ModelName):
    # compare the value of the path parameter with the enumeration member
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}
    # a string can be passed as comparison and compared with the value
    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}
    # You could also access the value "lenet" with ModelName.lenet.value.
    return {"model_name": model_name, "message": "Have some residuals"}

# If needed, a path could be passed as a parameter, using the Starlette option  
# "/files/{file_path:path}"
@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}