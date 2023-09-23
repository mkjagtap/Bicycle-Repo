from pydantic import BaseModel

class Bicycle(BaseModel):
    id: int
    brand:str
    colour:str
    price:float