from fastapi import FastAPI, Query
from pydantic import BaseModel
import math

app = FastAPI()

class Coordinates(BaseModel):
    lat: float
    lon: float

@app.get("/distance/")
async def calculate_distance(
    lat1: float = Query(..., description="Latitude of first point"),
    lon1: float = Query(..., description="Longitude of first point"),
    lat2: float = Query(..., description="Latitude of second point"),
    lon2: float = Query(..., description="Longitude of second point")
):
    # Calculate the distance using the formula
    distance = math.sqrt((lat2 - lat1)**2 + (lon2 - lon1)**2)
    
    return {
        "point1": {"latitude": lat1, "longitude": lon1},
        "point2": {"latitude": lat2, "longitude": lon2},
        "distance": distance
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)