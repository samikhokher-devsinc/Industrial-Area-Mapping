from sqlalchemy import Column, Integer, String, Float, Boolean, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Industry(Base):
    __tablename__ = "industries"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    sector = Column(String)
    lat = Column(Float)
    lng = Column(Float)
    owner = Column(String)
    contact = Column(String)
    website = Column(String)
    status = Column(Boolean)
    date = Column(Date)

class Zone(Base):
    __tablename__ = "zones"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    type = Column(String)
    polygon = Column(String)