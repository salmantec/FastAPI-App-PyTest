from fastapi import FastAPI

from .api import ping

app = FastAPI()


app.include_router(ping.router)