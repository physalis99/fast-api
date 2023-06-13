from fastapi import FastAPI
from enum import Enum
from pydantic import BaseModel

# create a FastAPI "instance"
app = FastAPI()


class ItemType(str, Enum):
    gold = "gold"
    silver = "silver"
    bronze = "bronze"


class Item(BaseModel):
    name: str
    type: ItemType
    price: float
    is_offer: bool = None


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/items/{item_id}")
# Declaring a parameter as None makes it optional.
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


@app.get("/items/types/{item_type}")
async def get_item_type(item_type: ItemType):
    if item_type is ItemType.gold:
        return {"item_name": "no.1", "item_type": item_type}
    return {"item_name": "other", "item_type": item_type}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}
