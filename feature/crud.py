from datetime import datetime
from typing import List
import shutil
import os
from fastapi import UploadFile
from fastapi import HTTPException
from sqlalchemy.orm import Session
from .models import  FeatureRelease
from .schemas import UpdateReleaseModelschema,ReleaseResponsechema
from sqlalchemy import UUID, desc
from sqlalchemy.orm import Session
from .models import Tag,FeatureRelease,PostDetails



def create_feature_release(db: Session, feature_release: UpdateReleaseModelschema):

    if feature_release.post_image_url:
        image_url = feature_release.post_image_url  # Just assign the URL directly
    else:
        image_url = None

    db_feature_release = FeatureRelease(
        title=feature_release.title,
        release_date=feature_release.release_date,
        release_version=feature_release.release_version,
        post_image_url=image_url,
        info=feature_release.info
    )
    
    db.add(db_feature_release)
    db.commit()  
    db.refresh(db_feature_release)


    if feature_release.post_details:
        for detail in feature_release.post_details:
            db_post_detail = PostDetails(
                title=detail.title,
                text_area=detail.text_area,
                feature_release_id=db_feature_release.id
            )
            db.add(db_post_detail)

    
    if feature_release.tags:
        for tag_data in feature_release.tags:
                db_tag = Tag(
                        name=tag_data.name, 
                        feature_release_id=db_feature_release.id
                    )
                db.add(db_tag)



    db.commit()  

    return db_feature_release



def feature_releases(db: Session, skip: int = 0, limit: int = 10):
    releases = (
         db.query(FeatureRelease)
         .order_by(desc(FeatureRelease.created_date))
         .offset(skip).limit(limit)
         .all()
    )
    for release in releases:
        release.uuid = str(release.uuid) if release.uuid else None
    
    return releases


def get_feature_by_id(db: Session, id: int):  # Ensure `id` is an integer
    print(f"Querying FeatureRelease with ID: {id}")
    # Fetch feature release by ID
    abx = db.query(FeatureRelease).filter(FeatureRelease.id == id).first()
    if not abx:
        print(f"No feature found with ID: {id}")
        return None
    print("Found feature with ID:", abx.id)
    return abx

def delete_feature_by_id(db:Session, id:int):
    feature = db.query(FeatureRelease).filter(FeatureRelease.id == id).first()
    if not feature:
        print(f"No feature found with ID: {id}")
    db.delete(feature)
    db.commit()
