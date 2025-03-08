from pydantic import BaseModel

class URLBase(BaseModel):
    target_url: str  # The URL which our shortened one will point to 

class URL(URLBase):
    is_active: bool 
    clicks: int

    class Config:
        orm_mode = True  # Telling Pydantic to work with a DB model

class URLinfo(URL):
    url: str
    admin_url: str
