from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List, Optional
from app.models.itinerary_schema import ItineraryRequest, ItineraryResponse, ItineraryHistoryItem
from app.models.itinerary_db import Itinerary as ItineraryModel
from app.models.user import User as UserModel
from app.services.gemini_service import generate_itinerary
from app.core.database import get_db
from app.routes.auth_routes import get_current_user
import logging

router = APIRouter()
logger = logging.getLogger(__name__)

@router.post("/itinerary", response_model=ItineraryResponse)
async def create_itinerary(
    request: ItineraryRequest, 
    db: Session = Depends(get_db),
    current_user: Optional[UserModel] = Depends(get_current_user)
):
    """
    Endpoint to generate an impressive travel itinerary and save it if logged in.
    """
    logger.info(f"Received API request for itinerary: Destination={request.destination}, Style={request.style}, Days={request.days}")
    try:
        itinerary_data = await generate_itinerary(request.destination, request.style, request.days)
        
        # Save to DB if user is authenticated
        if current_user:
            db_itinerary = ItineraryModel(
                user_id=current_user.id,
                destination=request.destination,
                style=request.style,
                days=request.days,
                content=itinerary_data
            )
            db.add(db_itinerary)
            db.commit()
            logger.info(f"Saved itinerary to database for user {current_user.email}")

        logger.info(f"Successfully generated API response for {request.destination}")
        return itinerary_data
    except Exception as e:
        logger.error(f"Error during execution: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/history", response_model=List[ItineraryHistoryItem])
def get_itinerary_history(
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user)
):
    """
    Get the travel history for the current logged-in user.
    """
    history = db.query(ItineraryModel).filter(
        ItineraryModel.user_id == current_user.id
    ).order_by(ItineraryModel.created_at.desc()).all()
    
    # Map trip_days from days (renaming for consistency with schema if needed)
    for item in history:
        item.trip_days = item.days
        
    return history
