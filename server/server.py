from fastapi import FastAPI
from pydantic import BaseModel
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s %(module)s %(levelname)s - %(message)s")
# file_handler = logging.FileHandler("log.txt")
file_handler = logging.StreamHandler()
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


class ServerStatus(BaseModel):
    status: bool


app = FastAPI()

ROUTE_SERVER_STATUS = "/"


@app.get(ROUTE_SERVER_STATUS, response_model=ServerStatus)
def server_is_online():
    logger.info("checked server status")
    return ServerStatus(status=True)
