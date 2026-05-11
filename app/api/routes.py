from fastapi import APIRouter
from app.schemas.schemas import IndustryCreate, ZoneCreate
from app.services.services import create_industry, get_industries, create_zone, get_zones

router = APIRouter()

@router.post("/industries")
def add_industry(data: IndustryCreate):
    return create_industry(data)

@router.get("/industries")
def list_industries():
    return get_industries()

@router.post("/zones")
def add_zone(data: ZoneCreate):
    return create_zone(data)

@router.get("/zones")
def list_zones():
    return get_zones()