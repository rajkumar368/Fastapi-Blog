from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy import create_mock_engine
from blog.database import engine
from blog import models

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{id}")
def read_item(id: int, q: Optional[str] = None):
    return {"item_id": id, "q": q}

@app.put("/items/{id}")
def update_item(id: int, item: Item):
    return {"item_name": item.name, "item_id": id}