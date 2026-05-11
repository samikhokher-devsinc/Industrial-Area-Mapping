from pydantic import BaseModel
from typing import Optional

class IndustryCreate(BaseModel):
    name: str
    sector: str
    lat: float
    lng: float
    owner: Optional[str]
    contact: Optional[str]
    website: Optional[str]
    status: bool

class ZoneCreate(BaseModel):
    name: str
    type: str
    polygon: str