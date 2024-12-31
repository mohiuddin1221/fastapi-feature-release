from fastapi import FastAPI,APIRouter, Depends, HTTPException
from database import get_db
from .schemas import CampusAmbassadorCreate
from sqlalchemy.orm import Session
from .crud import create_ambassador


app = APIRouter()

@app.post("/campus_ambassador")
async def create_campus_ambassador(campus_ambassador:CampusAmbassadorCreate, db: Session = Depends(get_db)):
    try:
        print(campus_ambassador.dict())
        return create_ambassador(db=db, campus_ambassador=campus_ambassador)
    except Exception as e:
        raise HTTPException(status_code=500, detail="Unable to create Campus Ambassador")