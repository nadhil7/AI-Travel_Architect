from google import genai
import json
import logging
from app.core.config import settings
from app.utils.prompt_builder import build_itinerary_prompt

logger = logging.getLogger(__name__)

# Initialize the Gemini client
try:
    if settings.GOOGLE_API_KEY:
        client = genai.Client(api_key=settings.GOOGLE_API_KEY)
        logger.info("Gemini API client successfully initialized.")
    else:
        client = None
        logger.warning("GOOGLE_API_KEY is not set. Gemini client not initialized.")
except Exception as e:
    client = None
    logger.error(f"Failed to initialize Gemini API client: {e}")

async def generate_itinerary(destination: str, style: str, days: int = 3) -> dict:
    """
    Calls the Gemini API to orchestrate generating a travel itinerary
    and validates the JSON output.
    """
    logger.info(f"generate_itinerary called with destination='{destination}', style='{style}', days={days}")
    
    if not client:
        logger.error("Attempted to generate itinerary but Gemini client is not initialized.")
        raise ValueError("Gemini API key is missing. Please set GOOGLE_API_KEY in the environment or .env file.")

    prompt = build_itinerary_prompt(destination, style, days)
    logger.debug(f"Prompt generated: {prompt}")
    
    try:
        logger.info("Sending request to Gemini API (gemini-2.5-flash)...")
        # Generate content enforcing JSON response
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
            config=genai.types.GenerateContentConfig(
                response_mime_type="application/json",
            ),
        )
        
        logger.info("Received response from Gemini API.")
        
        # Parse the JSON string from the response
        response_text = response.text
        if not response_text:
            logger.error("Empty response received from Gemini.")
            raise ValueError("Empty response received from Gemini.")
            
        logger.debug(f"Raw response text: {response_text}")
        itinerary_data = json.loads(response_text)
        logger.info("Successfully parsed Gemini response into JSON dictionary.")
        return itinerary_data
        
    except json.JSONDecodeError as e:
        logger.error(f"Failed to decode JSON from Gemini response: {e}. Raw response: {response_text}")
        raise ValueError("Received invalid JSON format from AI model.")
    except Exception as e:
        logger.error(f"Error generating itinerary with Gemini: {e}")
        raise e
