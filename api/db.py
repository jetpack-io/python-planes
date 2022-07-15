import os
from redis import StrictRedis


# use the specified Redis
password = os.environ.get("REDIS_PASSWORD") or None
host = os.environ.get("REDIS_HOST") or None
port = os.environ.get("REDIS_PORT") or "6379"

if not host:
    host = "localhost" # guess


print(f"Connecting to Redis: {host}:{port}")
redisClient = StrictRedis(host=host, port=int(port), password=password, decode_responses=True)
