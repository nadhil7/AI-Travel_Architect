from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from app.routes import itinerary, auth_routes
from app.core.database import engine, Base
from app.models.itinerary_db import Itinerary as ItineraryModel
import logging
import time

# Create database tables
Base.metadata.create_all(bind=engine)

# Configure logging at a basic level
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="AI Travel Architect API",
    description="Backend API to synthesize personalized travel itineraries via Gemini with User Auth.",
    version="1.1.0"
)

# Configure Cross-Origin Resource Sharing (CORS) to allow frontend connections
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()
    logger.info(f"Incoming Request: {request.method} {request.url}")
    
    response = await call_next(request)
    
    process_time = (time.time() - start_time) * 1000
    logger.info(f"Outgoing Response: {request.method} {request.url} - Status Code: {response.status_code} - Completed in {process_time:.2f}ms")
    return response

# Connect the routers
app.include_router(auth_routes.router, prefix="/api/auth", tags=["Authentication"])
app.include_router(itinerary.router, prefix="/api", tags=["Itinerary"])

@app.get("/health")
def health_check():
    """Simple status check"""
    logger.info("Health check endpoint pinged.")
    return {"status": "ok"}
