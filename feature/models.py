from sqlalchemy import UUID, Column, DateTime, Integer, String, Date, Text, ForeignKey, func
from sqlalchemy.orm import relationship
from database import Base 
import uuid


class FeatureRelease(Base):
    __tablename__ = "feature_releases"
 
    id = Column(Integer, primary_key=True, index=True)  
    uuid = Column(UUID(as_uuid=True), default=uuid.uuid4)
    title = Column(String, index=True)  
    release_date = Column(Date, nullable=True)
    release_version = Column(String, nullable=True)  
    post_image_url = Column(String, nullable=True)  
    info = Column(Text, nullable=True) 
    created_date = Column(DateTime, default=func.now(), nullable=False)  
    updated_date = Column(DateTime, default=func.now(), onupdate=func.now(), nullable=False) 


    # Add relationships to related tables
    post_details = relationship("PostDetails", back_populates="feature_release", cascade="all, delete-orphan", lazy="joined")
    tags = relationship("Tag", back_populates="feature_release", cascade="all, delete-orphan", lazy="joined")



class PostDetails(Base):
    __tablename__ = "post_details"

    id = Column(Integer, primary_key=True, index=True)  
    title = Column(String)  
    text_area = Column(Text)  
    feature_release_id = Column(Integer, ForeignKey('feature_releases.id')) 

    # Relationship to FeatureRelease
    feature_release = relationship("FeatureRelease", back_populates="post_details",lazy="joined")

class Tag(Base):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True, index=True)  
    name = Column(String, index=True)  
    feature_release_id = Column(Integer, ForeignKey('feature_releases.id'))

    # Relationship to FeatureRelease
    feature_release = relationship("FeatureRelease", back_populates="tags",lazy="joined")
