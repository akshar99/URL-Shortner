from . database import SessionLocal
db = SessionLocal()

from . models import URL

print(db.query(URL).all())