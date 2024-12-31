from sqlalchemy import Column, Integer, String, LargeBinary
from database import Base

class CampusAmbassador(Base):
    __tablename__ = 'campus_ambassador'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    phone_number = Column(String)
    email_address = Column(String, unique=True, index=True)
    university = Column(String)
    cv = Column(LargeBinary, nullable=True)  
    want_to_be = Column(String)
    in_any_club = Column(String)
    facebook = Column(String, nullable=True)
    instagram = Column(String, nullable=True)
    linkdin = Column(String, nullable=True)
