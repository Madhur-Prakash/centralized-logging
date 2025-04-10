from fastapi import APIRouter, status
import os
from . import models
from concurrent_log_handler import ConcurrentRotatingFileHandler
import logging

log_route = APIRouter()

def setup_logging():
    logger = logging.getLogger("central_log") # create logger
    if not logger.hasHandlers(): # check if handlers already exist
        logger.setLevel(logging.INFO) # set log level

        # create log directory if it doesn't exist
        log_dir = "logs/test"
        os.makedirs(log_dir, exist_ok=True)

        # create a file handler
        file_handler = ConcurrentRotatingFileHandler(
            os.path.join(log_dir, "central.log"), 
            maxBytes=10000, # 10KB 
            backupCount=500
        )
        file_handler.setLevel(logging.INFO) 
        #  create a console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        # create a formatter
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                                      datefmt="%Y-%m-%d %H:%M:%S")
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        #  add the handlers to the logger
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
    return logger

logger = setup_logging()

@log_route.post("/create_new_logs")
def new_log(data: models.newlog):
    if data.log_type == "info":
        logger.info(data.message)
        return{"message": "message logged", "status": status.HTTP_200_OK}

    elif data.log_type == "warning":
        logger.warning(data.message)
        return{"message": "message logged", "status": status.HTTP_200_OK}

    elif data.log_type == "error":
        logger.error(data.message)
        return{"message": "message logged", "status": status.HTTP_200_OK}