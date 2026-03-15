from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class ItineraryRequest(BaseModel):
    destination: str
    style: str
    days: int = 3

class DayActivities(BaseModel):
    day: int
    activities: List[str]

class ItineraryResponse(BaseModel):
    days: List[DayActivities]

class ItineraryResponseDB(ItineraryResponse):
    id: int
    destination: str
    style: str
    trip_days: int
    created_at: datetime

    class Config:
        from_attributes = True

class ItineraryHistoryItem(BaseModel):
    id: int
    destination: str
    style: str
    trip_days: int
    created_at: datetime

    class Config:
        from_attributes = True
