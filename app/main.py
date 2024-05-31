from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get('/')
def root():
    return {"message": "Hello World!"}


@app.get('/items/{item_id}')
def read_item(item_id: int, sort: Union[str, None] = 'Asc', limit: Union[int, None] = 5):
    return {
        "item_id": item_id,
        "sort": sort,
        "limit": limit
    }
    

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

@app.put("/items/{item_id}")
def update_items(item_id: int, item: Item):
    return {
        "item_name": item.name,
        "item_id": item_id
    }