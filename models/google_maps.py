import os
import requests

def get_nearby_hospitals(location):
    url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={location}&radius=5000&type=hospital&key={os.environ['GOOGLE_MAPS_API_KEY']}"
    response = requests.get(url)
    hospitals = response.json()
    if hospitals.get("results"):
        return hospitals["results"]
    else:
        return []
