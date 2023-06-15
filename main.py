from fastapi import FastAPI
from enum import Enum
from typing import Union
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


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}


@app.get("/items/types/{item_type}")
async def get_item_type(item_type: ItemType):
    if item_type is ItemType.gold:
        return {"item_name": "no.1", "item_type": item_type}
    return {"item_name": "other", "item_type": item_type}


@app.get("/items/actions/")
# Parameters for which no default value is set are mandatory.
# Parameters with default values are optional.
# None is null.
async def read_item_action(
    action: str, isReq: bool = False, req: Union[str, None] = None
):
    if isReq == True:
        return {
            "action": action,
            "isReq": isReq,
            "req": req,
        }
    return {"action": action}
