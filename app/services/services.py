from app.db.session import SessionLocal
from app.models.models import Industry, Zone

def create_industry(data):
    db = SessionLocal()
    obj = Industry(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_industries():
    db = SessionLocal()
    return db.query(Industry).all()

def create_zone(data):
    db = SessionLocal()
    obj = Zone(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_zones():
    db = SessionLocal()
    return db.query(Zone).all()