import secrets
from fastapi.responses import RedirectResponse
from fastapi import FastAPI, HTTPException, Depends, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import validators
from sqlalchemy.orm import Session
from testProject import schemas ,models
from .database import SessionLocal, engine, Base



app = FastAPI()
app.add_middleware(
    CORSMiddleware, 
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
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
def raise_not_found(request):
    message = f"URL {request.url} does not exist"
    raise HTTPException(status_code=404, detail=message)

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

@app.get("/{url_key}")
def forward_to_target_url(
        url_key: str,
        request: Request,
        db: Session = Depends(get_db)
    ):
    db_url = (
        db.query(models.URL)
        .filter(models.URL.key == url_key, models.URL.is_active)
        .first()
    )
    if db_url:
        return RedirectResponse(db_url.target_url)
    else:
        raise_not_found(request)