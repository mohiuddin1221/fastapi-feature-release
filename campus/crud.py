from fastapi import HTTPException
from sqlalchemy.orm import Session
from .models import CampusAmbassador
from .schemas import CampusAmbassadorCreate
def create_ambassador(db: Session, campus_ambassador: CampusAmbassadorCreate):
    try:
        # Check if the ambassador with the same email exists
        existing_ambassador = db.query(CampusAmbassador).filter(CampusAmbassador.email_address == campus_ambassador.email_address).first()
        if existing_ambassador:
            raise HTTPException(status_code=400, detail="Email address already registered")

        # Create a new ambassador object
        db_ambassador = CampusAmbassador(
            name=campus_ambassador.name,
            phone_number=campus_ambassador.phone_number,
            email_address=campus_ambassador.email_address,
            university=campus_ambassador.university,
            cv=campus_ambassador.cv,
            want_to_be=campus_ambassador.want_to_be,
            in_any_club=campus_ambassador.in_any_club,
            facebook=str(campus_ambassador.facebook) if campus_ambassador.facebook else None,  # Convert to string
            instagram=str(campus_ambassador.instagram) if campus_ambassador.instagram else None,  # Convert to string
            linkdin=str(campus_ambassador.linkdin) if campus_ambassador.linkdin else None,  # Convert to string
        )

        # Add the ambassador to the session
        db.add(db_ambassador)
        db.commit()  # Commit the transaction
        db.refresh(db_ambassador)  # Refresh to get the latest object from DB
        return db_ambassador
    except Exception as e:
        # If there's any error, rollback the transaction
        print(f"Error creating ambassador: {e}")
        db.rollback()  # Rollback transaction
        raise HTTPException(status_code=500, detail="Unable to create Campus Ambassador")
