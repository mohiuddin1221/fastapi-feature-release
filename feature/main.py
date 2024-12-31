from typing import List
from fastapi import FastAPI,APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from database import SessionLocal
from .schemas import (
    UpdateReleaseModelschema,
    ReleaseResponsechema,
    PostPreviewSchema
    
    )
from .crud import (
    create_feature_release,
    feature_releases ,
    get_feature_by_id,
    delete_feature_by_id
)


app = APIRouter()



@app.post("/feature_releases")
async def create__release(feature_release: UpdateReleaseModelschema,db: Session = Depends(get_db)):
    print(feature_release.dict())
    db_feature_release = create_feature_release(db=db, feature_release=feature_release)
    if not db_feature_release:
        raise HTTPException(status_code=400, detail="FeatureRelease creation failed")
    
    return db_feature_release


@app.get("/all_feature_releases", response_model=List[ReleaseResponsechema])
async def get_feature_releases(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    feature_releases_list = feature_releases(db, skip=skip, limit=limit)
    return feature_releases_list

@app.get("/single_feature/{id}")
async def get_feature_preview(id: int, db: Session = Depends(get_db)):
    print(f"Received ID: {id}")
    feature_post = get_feature_by_id(db, id)  # Ensure id consistency here
    print("feature_post:", feature_post)

    if not feature_post:
        print(f"Feature with ID {id} not found.")
        raise HTTPException(status_code=404, detail="Feature release not found")

    return feature_post

@app.delete("/delete/{id}")
async def delete_feature(id: int, db:Session = Depends(get_db)):
    print(f"Deleting feature with ID: {id}")
    message =  delete_feature_by_id(db, id)
    return message