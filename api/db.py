import os
from redis import StrictRedis


# use the specified Redis
password = os.environ.get("REDIS_PASSWORD") or None
host = os.environ.get("REDIS_HOST") or None
port = os.environ.get("REDIS_PORT") or "6379"

if not host and not password:
    # running in Jetpack.io cluster?
    password = os.environ.get("JETPACK_RUNTIME_REDIS_PASSWORD")
    if password:
        host = "jetpack-runtime-redis-master"

if not host:
    host = "localhost" # guess


print(f"Connecting to Redis: {host}:{port}")
redisClient = StrictRedis(host=host, port=int(port), password=password, decode_responses=True)
