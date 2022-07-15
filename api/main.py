import asyncio
import json
import uvicorn
from starlette.responses import FileResponse
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import os
from db import redisClient


app = FastAPI(title="app")

@app.get("/api/flight")
async def get_flights():
    data = redisClient.get("planes")
    result = json.loads(data) if data else []
    return result

@app.get("/")
async def read_index():
    return FileResponse("public/index.html")

app.mount("/", StaticFiles(directory="public"), name="public")

if __name__ == "__main__":
    # start the web server
    port = os.environ.get("PORT") or "8080"
    uvicorn.run(app, host="0.0.0.0", port=int(port))
