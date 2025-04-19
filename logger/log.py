from fastapi import APIRouter, status, Request
import os
from . import models
import traceback
from concurrent_log_handler import ConcurrentRotatingFileHandler
import logging

log_route = APIRouter()

def setup_logging(directory: str, filename: str, log_service_name: str): # log_service _name is the {name} parameter in logging.Formatter
    logger = logging.getLogger(log_service_name) # create logger
    if not logger.hasHandlers(): # check if handlers already exist
        logger.setLevel(logging.INFO) # set log level

        # create log directory if it doesn't exist
        os.makedirs(directory, exist_ok=True)

        # create a file handler
        file_handler = ConcurrentRotatingFileHandler(
            os.path.join(directory, filename), 
            maxBytes=100000, # 10KB 
            backupCount=500
        )
        file_handler.setLevel(logging.INFO) 
        #  create a console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        # create a formatter
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(pathname)s - %(filename)s - %(lineno)d" , datefmt="%Y-%m-%d %H:%M:%S")
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        #  add the handlers to the logger
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
    return logger


@log_route.post("/backend/create_new_logs")
def new_backend_log(request: Request, data: models.newlog):
    incoming_header = request.headers.get("X-Source-Endpoint")
    print(incoming_header)

    try:

        if incoming_header == "/api/backend/Auth":
            logger = setup_logging("Backend/Auth", "auth.log","auth_log") # logger instance
            print("auth hit")
            if data.log_type == "info":
                print("INFO hit")
                logger.info(data.message)
                return{"message": "message logged", "status": status.HTTP_200_OK}

            elif data.log_type == "warning":
                print("WARNING hit")
                logger.warning(data.message)
                return{"message": "message logged", "status": status.HTTP_200_OK}

            elif data.log_type == "error":
                print("ERROR hit")
                logger.error(data.message)
                return{"message": "message logged", "status": status.HTTP_200_OK}

        elif incoming_header == "/api/backend/Appointment":
            logger = setup_logging("Backend/Appointment", "appointment.log","appointment_log") # logger instance
            print("appointment hit")
            if data.log_type == "info":
                print("INFO hit")
                logger.info(data.message)
                return{"message": "message logged", "status": status.HTTP_200_OK}

            elif data.log_type == "warning":
                print("WARNING hit")
                logger.warning(data.message)
                return{"message": "message logged", "status": status.HTTP_200_OK}

            elif data.log_type == "error":
                print("ERROR hit")
                logger.error(data.message)
                return{"message": "message logged", "status": status.HTTP_200_OK}
        
        elif incoming_header == "/api/backend/MedicalRecord":
            logger = setup_logging("Backend/MedicalRecord", "medicalrecord.log","medicalrecord_log") # logger instance
            print("MedicalRecord hit")
            if data.log_type == "info":
                print("INFO hit")
                logger.info(data.message)
                return{"message": "message logged", "status": status.HTTP_200_OK}

            elif data.log_type == "warning":
                print("WARNING hit")
                logger.warning(data.message)
                return{"message": "message logged", "status": status.HTTP_200_OK}

            elif data.log_type == "error":
                print("ERROR hit")
                logger.error(data.message)
                return{"message": "message logged", "status": status.HTTP_200_OK}

        elif incoming_header == "/api/backend/Message":
            logger = setup_logging("Backend/Message", "message.log","message_log") # logger instance
            print("Message hit")
            if data.log_type == "info":
                print("INFO hit")
                logger.info(data.message)
                return{"message": "message logged", "status": status.HTTP_200_OK}

            elif data.log_type == "warning":
                print("WARNING hit")
                logger.warning(data.message)
                return{"message": "message logged", "status": status.HTTP_200_OK}

            elif data.log_type == "error":
                print("ERROR hit")
                logger.error(data.message)
                return{"message": "message logged", "status": status.HTTP_200_OK}

        elif incoming_header == "/api/backend/ContactUs":
            logger = setup_logging("Backend/ContactUs", "contactus.log","contactus_log") # logger instance
            print("ContactUs hit")
            if data.log_type == "info":
                print("INFO hit")
                logger.info(data.message)
                return{"message": "message logged", "status": status.HTTP_200_OK}

            elif data.log_type == "warning":
                print("WARNING hit")
                logger.warning(data.message)
                return{"message": "message logged", "status": status.HTTP_200_OK}

            elif data.log_type == "error":
                print("ERROR hit")
                logger.error(data.message)
                return{"message": "message logged", "status": status.HTTP_200_OK}
    except Exception as e:
        formatted_error = traceback.format_exc()
        print("Error creating log: ", formatted_error)
        logger.error(f"Error creating log: {formatted_error}")
        return {"message": "Error creating log", "status": status.HTTP_500_INTERNAL_SERVER_ERROR}
        
@log_route.post("/app/create_new_logs")
def new_app_log(request: Request, data: models.newlog):
    incoming_header = request.headers.get("X-Source-Endpoint")
    print(incoming_header)

    try:

        if incoming_header == "/api/app/Auth":
            logger = setup_logging("/root/logs/App/Auth", "auth.log","auth_log") # logger instance
            print("auth hit")
            if data.log_type == "info":
                print("INFO hit")
                logger.info(data.message)
                return{"message": "message logged", "status": status.HTTP_200_OK}

            elif data.log_type == "warning":
                print("WARNING hit")
                logger.warning(data.message)
                return{"message": "message logged", "status": status.HTTP_200_OK}

            elif data.log_type == "error":
                print("ERROR hit")
                logger.error(data.message)
                return{"message": "message logged", "status": status.HTTP_200_OK}

        elif incoming_header == "/api/app/Appointment":
            logger = setup_logging("/root/logs/App/Appointment", "appointment.log","appointment_log") # logger instance
            print("appointment hit")
            if data.log_type == "info":
                print("INFO hit")
                logger.info(data.message)
                return{"message": "message logged", "status": status.HTTP_200_OK}

            elif data.log_type == "warning":
                print("WARNING hit")
                logger.warning(data.message)
                return{"message": "message logged", "status": status.HTTP_200_OK}

            elif data.log_type == "error":
                print("ERROR hit")
                logger.error(data.message)
                return{"message": "message logged", "status": status.HTTP_200_OK}
        
        elif incoming_header == "/api/app/MedicalRecord":
            logger = setup_logging("/root/logs/App/MedicalRecord", "medicalrecord.log","medicalrecord_log") # logger instance
            print("MedicalRecord hit")
            if data.log_type == "info":
                print("INFO hit")
                logger.info(data.message)
                return{"message": "message logged", "status": status.HTTP_200_OK}

            elif data.log_type == "warning":
                print("WARNING hit")
                logger.warning(data.message)
                return{"message": "message logged", "status": status.HTTP_200_OK}

            elif data.log_type == "error":
                print("ERROR hit")
                logger.error(data.message)
                return{"message": "message logged", "status": status.HTTP_200_OK}

        elif incoming_header == "/api/app/Message":
            logger = setup_logging("/root/logs/App/Message", "message.log","message_log") # logger instance
            print("Message hit")
            if data.log_type == "info":
                print("INFO hit")
                logger.info(data.message)
                return{"message": "message logged", "status": status.HTTP_200_OK}

            elif data.log_type == "warning":
                print("WARNING hit")
                logger.warning(data.message)
                return{"message": "message logged", "status": status.HTTP_200_OK}

            elif data.log_type == "error":
                print("ERROR hit")
                logger.error(data.message)
                return{"message": "message logged", "status": status.HTTP_200_OK}

        elif incoming_header == "/api/app/ContactUs":
            logger = setup_logging("/root/logs/App/ContactUs", "contactus.log","contactus_log") # logger instance
            print("ContactUs hit")
            if data.log_type == "info":
                print("INFO hit")
                logger.info(data.message)
                return{"message": "message logged", "status": status.HTTP_200_OK}

            elif data.log_type == "warning":
                print("WARNING hit")
                logger.warning(data.message)
                return{"message": "message logged", "status": status.HTTP_200_OK}

            elif data.log_type == "error":
                print("ERROR hit")
                logger.error(data.message)
                return{"message": "message logged", "status": status.HTTP_200_OK}

    except Exception as e:
        formatted_error = traceback.format_exc()
        print("Error creating log: ", formatted_error)
        logger.error(f"Error creating log: {formatted_error}")
        return {"message": "Error creating log", "status": status.HTTP_500_INTERNAL_SERVER_ERROR}

@log_route.post("/website/create_new_logs")
def new_website_log(request: Request, data: models.newlog):
    incoming_header = request.headers.get("X-Source-Endpoint")
    print(incoming_header)

    try:

        if incoming_header == "/api/website/Auth":
            logger = setup_logging("/root/logs/Website/Auth", "auth.log","auth_log") # logger instance
            print("auth hit")
            if data.log_type == "info":
                print("INFO hit")
                logger.info(data.message)
                return{"message": "message logged", "status": status.HTTP_200_OK}

            elif data.log_type == "warning":
                print("WARNING hit")
                logger.warning(data.message)
                return{"message": "message logged", "status": status.HTTP_200_OK}

            elif data.log_type == "error":
                print("ERROR hit")
                logger.error(data.message)
                return{"message": "message logged", "status": status.HTTP_200_OK}

        elif incoming_header == "/api/website/Appointment":
            logger = setup_logging("/root/logs/Website/websiteappointment", "websiteointment.log","websiteointment_log") # logger instance
            print("websiteointment hit")
            if data.log_type == "info":
                print("INFO hit")
                logger.info(data.message)
                return{"message": "message logged", "status": status.HTTP_200_OK}

            elif data.log_type == "warning":
                print("WARNING hit")
                logger.warning(data.message)
                return{"message": "message logged", "status": status.HTTP_200_OK}

            elif data.log_type == "error":
                print("ERROR hit")
                logger.error(data.message)
                return{"message": "message logged", "status": status.HTTP_200_OK}
        
        elif incoming_header == "/api/website/MedicalRecord":
            logger = setup_logging("/root/logs/Website/MedicalRecord", "medicalrecord.log","medicalrecord_log") # logger instance
            print("MedicalRecord hit")
            if data.log_type == "info":
                print("INFO hit")
                logger.info(data.message)
                return{"message": "message logged", "status": status.HTTP_200_OK}

            elif data.log_type == "warning":
                print("WARNING hit")
                logger.warning(data.message)
                return{"message": "message logged", "status": status.HTTP_200_OK}

            elif data.log_type == "error":
                print("ERROR hit")
                logger.error(data.message)
                return{"message": "message logged", "status": status.HTTP_200_OK}

        elif incoming_header == "/api/website/Message":
            logger = setup_logging("/root/logs/Website/Message", "message.log","message_log") # logger instance
            print("Message hit")
            if data.log_type == "info":
                print("INFO hit")
                logger.info(data.message)
                return{"message": "message logged", "status": status.HTTP_200_OK}

            elif data.log_type == "warning":
                print("WARNING hit")
                logger.warning(data.message)
                return{"message": "message logged", "status": status.HTTP_200_OK}

            elif data.log_type == "error":
                print("ERROR hit")
                logger.error(data.message)
                return{"message": "message logged", "status": status.HTTP_200_OK}

        elif incoming_header == "/api/website/ContactUs":
            logger = setup_logging("/root/logs/Website/ContactUs", "contactus.log","contactus_log") # logger instance
            print("ContactUs hit")
            if data.log_type == "info":
                print("INFO hit")
                logger.info(data.message)
                return{"message": "message logged", "status": status.HTTP_200_OK}

            elif data.log_type == "warning":
                print("WARNING hit")
                logger.warning(data.message)
                return{"message": "message logged", "status": status.HTTP_200_OK}

            elif data.log_type == "error":
                print("ERROR hit")
                logger.error(data.message)
                return{"message": "message logged", "status": status.HTTP_200_OK}
            
    except Exception as e:
        formatted_error = traceback.format_exc()
        print("Error creating log: ", formatted_error)
        logger.error(f"Error creating log: {formatted_error}")
        return {"message": "Error creating log", "status": status.HTTP_500_INTERNAL_SERVER_ERROR}