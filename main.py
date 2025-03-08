import secrets

from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import Optional
import validators
from sqlalchemy.orm import Session
from testProject import schemas ,models
from .database import SessionLocal, engine, Base



app = FastAPI()
models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


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

#this is for creating a url using a post method
@app.post("/url", response_model= schemas.URLinfo)
async def create_url(url : schemas.URLBase, db: Session= Depends(get_db)):
    if not validators.url(url.target_url):
        raiseBadRequest(message="You have provided a wrong link")
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    key = "".join(secrets.choice(chars) for _ in range(5))
    secret_key = "".join(secrets.choice(chars) for _ in range(8))
    db_url = models.URL(target_url= url.target_url, key=key, secret_key=secret_key)
    db.add(db_url)
    db.commit()
    db.refresh(db_url)
    db_url.url = key
    db_url.admin_url = secret_key
    return db_url