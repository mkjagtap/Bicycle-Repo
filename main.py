# Author : Tanmay Borse

from fastapi import FastAPI
from bicycle import Bicycle

print(f"inside home function")
print(f"inside new home function")

app = FastAPI()
bicycle_list = []


@app.get("/")
def home():
    print(f"inside home function")
    return{"message": "Welcome to the Mukesh's bicycle shop!"}

@app.post("/")
def add_new_bicycle(bicycle: Bicycle):
    print(f"Inside add new bicycle method")
    return bicycle_list

@app.get("/bicycle")
def get_bicycle():
    print(f"inside get bicycle")
    return {"available_bicycle": bicycle_list}