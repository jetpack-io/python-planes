import asyncio
from datetime import datetime
import json
from jetpack import cron
from requests import get
from db import redisClient


# So we can serialize a list
class SetEncoder(json.JSONEncoder):
    def default(self, obj):
       if isinstance(obj, set):
          return list(obj)
       return json.JSONEncoder.default(self, obj)

# array to object
def pivot_item(item, loadDate: str):
    (ica024, callsign, originCountry, timePositionNum, lastContactNum, longitude, latitude, baroAltitude, onGround, velocity, trueTrack, verticalRate, sensors, altitude, squawk, spi, positionSource) = item

    lastContact = datetime.utcfromtimestamp(lastContactNum).isoformat()
    timePosition = datetime.utcfromtimestamp(timePositionNum).isoformat() if timePositionNum else None
    if callsign:
        callsign = callsign.rstrip()

    flight = {
        "loadDate":loadDate,
        "ica024":ica024,
        "callsign":callsign,
        "originCountry":originCountry,
        "timePosition":timePosition,
        "lastContact":lastContact,
        "longitude":longitude,
        "latitude":latitude,
        "baroAltitude":baroAltitude,
        "onGround":onGround,
        "velocity":velocity,
        "trueTrack":trueTrack,
        "verticalRate":verticalRate,
        "altitude":altitude,
        "squawk":squawk,
        "spi":spi,
        "positionSource":positionSource
    }
    return flight

@cron.repeat(schedule="* * * * *") # every minute
async def load_data():
    url = "https://opensky-network.org/api/states/all"
    opensky_data = get(url).json()
    load_date = datetime.utcfromtimestamp(opensky_data["time"]).isoformat()
    states = opensky_data["states"]
    result = list(map(lambda item: pivot_item(item, load_date), states))
    redisClient.set("planes", json.dumps(result, cls=SetEncoder))
    print(f'Loaded flights: {load_date}')
