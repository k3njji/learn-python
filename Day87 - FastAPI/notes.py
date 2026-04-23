# uvicorn main:app --reload
# curl -X POST -H "Content-Type: application/json" 'http://127.0.0.1:8000/items?item=apple'
# curl -X POST http://127.0.0.1:8000/items -H "Content-Type: application/json" -d '{"text": "apple", "is_done": false}'

from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel
from typing import Optional, List
import uvicorn

class Item(BaseModel):
    text: str
    is_done: bool = False

app = FastAPI()

items = []

@app.get('/')
def home():
    return {'message': 'Hello FastApi'}

@app.get('/items', response_model=list[Item])
def get_all_items(limit: int = 10):
    return items[:limit]

@app.post('/items', response_model=list[Item])
def create_item(item: Item):
    items.append(item)
    return items

@app.get('/items/{item_id}', response_model=Item)
def get_item(item_id: int):
    if item_id >= len(items):
        raise HTTPException(status_code=404, detail='item is not found')
    return items[item_id]