from google.adk.agents import Agent
from google.adk.tools import google_search
from datetime import datetime
from datetime import datetime
from zoneinfo import ZoneInfo
import os 
from dotenv import load_dotenv

load_dotenv()

# Mapping of cities to timezones
CITY_TIMEZONES = {
    "mumbai": "Asia/Kolkata",
    "delhi": "Asia/Kolkata",
    "new york": "America/New_York",
    "los angeles": "America/Los_Angeles",
    "london": "Europe/London",
    "paris": "Europe/Paris",
    "dubai": "Asia/Dubai",
    "tokyo": "Asia/Tokyo",
    "sydney": "Australia/Sydney"
}

def get_current_time(city: str) -> dict:
    """Returns the current time in the specified city."""
    city_lower = city.lower()
    
    if city_lower not in CITY_TIMEZONES:
        return {
            "status": "error",
            "message": f"City '{city}' not supported",
            "supported_cities": list(CITY_TIMEZONES.keys())
        }

    timezone = CITY_TIMEZONES[city_lower]
    current_time = datetime.now(ZoneInfo(timezone)).strftime("%Y-%m-%d %I:%M:%S %p")

    return {
        "status": "success",
        "city": city,
        "time": current_time
    }


root_agent = Agent(
    name='simple_adk_agent',
    model='gemini-2.0-flash',
    description="Tells the current time in a specified city.",
    instruction="You are a helpful assistant that tells the current time in cities. Use the 'get_current_time' tool for this purpose.",
    tools=[get_current_time],
)