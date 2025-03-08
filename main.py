

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
import validators
from . import schemas


app = FastAPI()

class item(BaseModel):
    name: str
    description: Optional[str]  = None
    ID : int
    price : float
    info : Optional[str]  = None

def raiseBadRequest(message):
    raise HTTPException(status_code=400, detail=message)



@app.get("/")
async def read_root():
    return {"Welcome to URL Shortner API : "}

@app.post("/url")
async def create_url(url : schemas.URLBase):
    if not validators.url(url.target_url):
        raiseBadRequest(message="You have provided a wrong link")
    return f"TODO : Create DB Entry for: {url.target_url}"