from fastapi import FastAPI
from logger.log import log_route

app = FastAPI()
app.include_router(log_route)
