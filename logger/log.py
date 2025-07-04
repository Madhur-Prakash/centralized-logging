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
        elif incoming_header == "/api/backend/Connect":
            logger = setup_logging("Backend/Connect", "connect.log","connect_log")
            print("Connect hit")
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
        elif incoming_header == "/api/backend/Profile":
            logger = setup_logging("Backend/Profile", "profile.log","profile_log")
            print("Profile hit")
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
        elif incoming_header == "/api/backend/Patient_public_profile":
            logger = setup_logging("Backend/Patient_public_profile", "patient_public_profile.log","patient_public_profile_log")
            print("Patient_public_profile hit")
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
        elif incoming_header == "/api/backend/Doctor_public_profile":
            logger = setup_logging("Backend/Doctor_public_profile", "doctor_public_profile.log","doctor_public_profile_log")
            print("Doctor_public_profile hit")
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
        elif incoming_header == "/api/backend/Search":
            logger = setup_logging("Backend/Search", "search.log","search_log")
            print("Search hit")
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
        elif incoming_header == "/api/backend/Report_problem":
            logger = setup_logging("Backend/Report_problem", "report_problem.log","report_problem_log")
            print("Report_problem hit")
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
        elif incoming_header == "/api/backend/Img_to_json":
            logger = setup_logging("Backend/Img_to_json", "img_to_json.log","img_to_json_log")
            print("Img_to_json hit")
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
        elif incoming_header == "/api/backend/Pdf_to_json":
            logger = setup_logging("Backend/Pdf_to_json", "pdf_to_json.log","pdf_to_json_log")
            print("Pdf_to_json hit")
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
        elif incoming_header == "/api/backend/Timeline":
            logger = setup_logging("Backend/Timeline", "timeline.log","timeline_log")
            print("Timeline hit")
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
        
#
# ***************** these endpoints are not used anymore, but kept for reference *****************
# @log_route.post("/app/create_new_logs")
# def new_app_log(request: Request, data: models.newlog):
#     incoming_header = request.headers.get("X-Source-Endpoint")
#     print(incoming_header)

#     try:

#         if incoming_header == "/api/app/Auth":
#             logger = setup_logging("/root/logs/App/Auth", "auth.log","auth_log") # logger instance
#             print("auth hit")
#             if data.log_type == "info":
#                 print("INFO hit")
#                 logger.info(data.message)
#                 return{"message": "message logged", "status": status.HTTP_200_OK}

#             elif data.log_type == "warning":
#                 print("WARNING hit")
#                 logger.warning(data.message)
#                 return{"message": "message logged", "status": status.HTTP_200_OK}

#             elif data.log_type == "error":
#                 print("ERROR hit")
#                 logger.error(data.message)
#                 return{"message": "message logged", "status": status.HTTP_200_OK}
#         elif incoming_header == "/api/app/Appointment":
#             logger = setup_logging("/root/logs/App/Appointment", "appointment.log","appointment_log") # logger instance
#             print("appointment hit")
#             if data.log_type == "info":
#                 print("INFO hit")
#                 logger.info(data.message)
#                 return{"message": "message logged", "status": status.HTTP_200_OK}

#             elif data.log_type == "warning":
#                 print("WARNING hit")
#                 logger.warning(data.message)
#                 return{"message": "message logged", "status": status.HTTP_200_OK}

#             elif data.log_type == "error":
#                 print("ERROR hit")
#                 logger.error(data.message)
#                 return{"message": "message logged", "status": status.HTTP_200_OK}
        
#         elif incoming_header == "/api/app/MedicalRecord":
#             logger = setup_logging("/root/logs/App/MedicalRecord", "medicalrecord.log","medicalrecord_log") # logger instance
#             print("MedicalRecord hit")
#             if data.log_type == "info":
#                 print("INFO hit")
#                 logger.info(data.message)
#                 return{"message": "message logged", "status": status.HTTP_200_OK}

#             elif data.log_type == "warning":
#                 print("WARNING hit")
#                 logger.warning(data.message)
#                 return{"message": "message logged", "status": status.HTTP_200_OK}

#             elif data.log_type == "error":
#                 print("ERROR hit")
#                 logger.error(data.message)
#                 return{"message": "message logged", "status": status.HTTP_200_OK}

#         elif incoming_header == "/api/app/Message":
#             logger = setup_logging("/root/logs/App/Message", "message.log","message_log") # logger instance
#             print("Message hit")
#             if data.log_type == "info":
#                 print("INFO hit")
#                 logger.info(data.message)
#                 return{"message": "message logged", "status": status.HTTP_200_OK}

#             elif data.log_type == "warning":
#                 print("WARNING hit")
#                 logger.warning(data.message)
#                 return{"message": "message logged", "status": status.HTTP_200_OK}

#             elif data.log_type == "error":
#                 print("ERROR hit")
#                 logger.error(data.message)
#                 return{"message": "message logged", "status": status.HTTP_200_OK}

#         elif incoming_header == "/api/app/ContactUs":
#             logger = setup_logging("/root/logs/App/ContactUs", "contactus.log","contactus_log") # logger instance
#             print("ContactUs hit")
#             if data.log_type == "info":
#                 print("INFO hit")
#                 logger.info(data.message)
#                 return{"message": "message logged", "status": status.HTTP_200_OK}

#             elif data.log_type == "warning":
#                 print("WARNING hit")
#                 logger.warning(data.message)
#                 return{"message": "message logged", "status": status.HTTP_200_OK}

#             elif data.log_type == "error":
#                 print("ERROR hit")
#                 logger.error(data.message)
#                 return{"message": "message logged", "status": status.HTTP_200_OK}
#         elif incoming_header == "/api/app/Connect":
#             logger = setup_logging("/root/logs/App/Connect", "connect.log","connect_log")
#             print("Connect hit")
#             if data.log_type == "info":
#                 print("INFO hit")
#                 logger.info(data.message)
#                 return{"message": "message logged", "status": status.HTTP_200_OK}
#             elif data.log_type == "warning":
#                 print("WARNING hit")
#                 logger.warning(data.message)
#                 return{"message": "message logged", "status": status.HTTP_200_OK}
#             elif data.log_type == "error":
#                 print("ERROR hit")
#                 logger.error(data.message)
#                 return{"message": "message logged", "status": status.HTTP_200_OK}
#         elif incoming_header == "/api/app/Profile":
#             logger = setup_logging("/root/logs/App/Profile", "profile.log","profile_log")
#             print("Profile hit")
#             if data.log_type == "info":
#                 print("INFO hit")
#                 logger.info(data.message)
#                 return{"message": "message logged", "status": status.HTTP_200_OK}
#             elif data.log_type == "warning":
#                 print("WARNING hit")
#                 logger.warning(data.message)
#                 return{"message": "message logged", "status": status.HTTP_200_OK}
#             elif data.log_type == "error":
#                 print("ERROR hit")
#                 logger.error(data.message)
#                 return{"message": "message logged", "status": status.HTTP_200_OK}
#         elif incoming_header == "/api/app/Patient_public_profile":
#             logger = setup_logging("/root/logs/App/Patient_public_profile", "patient_public_profile.log","patient_public_profile_log")
#             print("Patient_public_profile hit")
#             if data.log_type == "info":
#                 print("INFO hit")
#                 logger.info(data.message)
#                 return{"message": "message logged", "status": status.HTTP_200_OK}
#             elif data.log_type == "warning":
#                 print("WARNING hit")
#                 logger.warning(data.message)
#                 return{"message": "message logged", "status": status.HTTP_200_OK}
#             elif data.log_type == "error":
#                 print("ERROR hit")
#                 logger.error(data.message)
#                 return{"message": "message logged", "status": status.HTTP_200_OK}
#         elif incoming_header == "/api/app/Doctor_public_profile":
#             logger = setup_logging("/root/logs/App/Doctor_public_profile", "doctor_public_profile.log","doctor_public_profile_log")
#             print("Doctor_public_profile hit")
#             if data.log_type == "info":
#                 print("INFO hit")
#                 logger.info(data.message)
#                 return{"message": "message logged", "status": status.HTTP_200_OK}
#             elif data.log_type == "warning":
#                 print("WARNING hit")
#                 logger.warning(data.message)
#                 return{"message": "message logged", "status": status.HTTP_200_OK}
#             elif data.log_type == "error":
#                 print("ERROR hit")
#                 logger.error(data.message)
#                 return{"message": "message logged", "status": status.HTTP_200_OK}
#         elif incoming_header == "/api/app/Report_problem":
#             logger = setup_logging("/root/logs/App/Report_problem", "report_problem.log","report_problem_log")
#             print("Report_problem hit")
#             if data.log_type == "info":
#                 print("INFO hit")
#                 logger.info(data.message)
#                 return{"message": "message logged", "status": status.HTTP_200_OK}
#             elif data.log_type == "warning":
#                 print("WARNING hit")
#                 logger.warning(data.message)
#                 return{"message": "message logged", "status": status.HTTP_200_OK}
#             elif data.log_type == "error":
#                 print("ERROR hit")
#                 logger.error(data.message)
#                 return{"message": "message logged", "status": status.HTTP_200_OK}
#         elif incoming_header == "/api/app/Search":
#             logger = setup_logging("/root/logs/App/Search", "search.log","search_log")
#             print("Search hit")
#             if data.log_type == "info":
#                 print("INFO hit")
#                 logger.info(data.message)
#                 return{"message": "message logged", "status": status.HTTP_200_OK}
#             elif data.log_type == "warning":
#                 print("WARNING hit")
#                 logger.warning(data.message)
#                 return{"message": "message logged", "status": status.HTTP_200_OK}
#             elif data.log_type == "error":
#                 print("ERROR hit")
#                 logger.error(data.message)
#                 return{"message": "message logged", "status": status.HTTP_200_OK}
#         elif incoming_header == "/api/app/Img_to_json":
#             logger = setup_logging("/root/logs/App/Img_to_json", "img_to_json.log","img_to_json_log")
#             print("Img_to_json hit")
#             if data.log_type == "info":
#                 print("INFO hit")
#                 logger.info(data.message)
#                 return{"message": "message logged", "status": status.HTTP_200_OK}
#             elif data.log_type == "warning":
#                 print("WARNING hit")
#                 logger.warning(data.message)
#                 return{"message": "message logged", "status": status.HTTP_200_OK}
#             elif data.log_type == "error":
#                 print("ERROR hit")
#                 logger.error(data.message)
#                 return{"message": "message logged", "status": status.HTTP_200_OK}
            
#         elif incoming_header == "/api/app/Pdf_to_json":
#             logger = setup_logging("/root/logs/App/Pdf_to_json", "pdf_to_json.log","pdf_to_json_log")
#             print("Pdf_to_json hit")
#             if data.log_type == "info":
#                 print("INFO hit")
#                 logger.info(data.message)
#                 return{"message": "message logged", "status": status.HTTP_200_OK}
#             elif data.log_type == "warning":
#                 print("WARNING hit")
#                 logger.warning(data.message)
#                 return{"message": "message logged", "status": status.HTTP_200_OK}
#             elif data.log_type == "error":
#                 print("ERROR hit")
#                 logger.error(data.message)
#                 return{"message": "message logged", "status": status.HTTP_200_OK}
            
#         elif incoming_header == "/api/app/Timeline":
#             logger = setup_logging("/root/logs/App/Timeline", "timeline.log","timeline_log")
#             print("Timeline hit")
#             if data.log_type == "info":
#                 print("INFO hit")
#                 logger.info(data.message)
#                 return{"message": "message logged", "status": status.HTTP_200_OK}
#             elif data.log_type == "warning":
#                 print("WARNING hit")
#                 logger.warning(data.message)
#                 return{"message": "message logged", "status": status.HTTP_200_OK}
#             elif data.log_type == "error":
#                 print("ERROR hit")
#                 logger.error(data.message)
#                 return{"message": "message logged", "status": status.HTTP_200_OK}

#     except Exception as e:
#         formatted_error = traceback.format_exc()
#         print("Error creating log: ", formatted_error)
#         logger.error(f"Error creating log: {formatted_error}")
#         return {"message": "Error creating log", "status": status.HTTP_500_INTERNAL_SERVER_ERROR}

# @log_route.post("/website/create_new_logs")
# def new_website_log(request: Request, data: models.newlog):
#     incoming_header = request.headers.get("X-Source-Endpoint")
#     print(incoming_header)

#     try:

#         if incoming_header == "/api/website/Auth":
#             logger = setup_logging("/root/logs/Website/Auth", "auth.log","auth_log") # logger instance
#             print("auth hit")
#             if data.log_type == "info":
#                 print("INFO hit")
#                 logger.info(data.message)
#                 return{"message": "message logged", "status": status.HTTP_200_OK}

#             elif data.log_type == "warning":
#                 print("WARNING hit")
#                 logger.warning(data.message)
#                 return{"message": "message logged", "status": status.HTTP_200_OK}

#             elif data.log_type == "error":
#                 print("ERROR hit")
#                 logger.error(data.message)
#                 return{"message": "message logged", "status": status.HTTP_200_OK}

#         elif incoming_header == "/api/website/Appointment":
#             logger = setup_logging("/root/logs/Website/websiteappointment", "websiteointment.log","websiteointment_log") # logger instance
#             print("websiteointment hit")
#             if data.log_type == "info":
#                 print("INFO hit")
#                 logger.info(data.message)
#                 return{"message": "message logged", "status": status.HTTP_200_OK}

#             elif data.log_type == "warning":
#                 print("WARNING hit")
#                 logger.warning(data.message)
#                 return{"message": "message logged", "status": status.HTTP_200_OK}

#             elif data.log_type == "error":
#                 print("ERROR hit")
#                 logger.error(data.message)
#                 return{"message": "message logged", "status": status.HTTP_200_OK}
        
#         elif incoming_header == "/api/website/MedicalRecord":
#             logger = setup_logging("/root/logs/Website/MedicalRecord", "medicalrecord.log","medicalrecord_log") # logger instance
#             print("MedicalRecord hit")
#             if data.log_type == "info":
#                 print("INFO hit")
#                 logger.info(data.message)
#                 return{"message": "message logged", "status": status.HTTP_200_OK}

#             elif data.log_type == "warning":
#                 print("WARNING hit")
#                 logger.warning(data.message)
#                 return{"message": "message logged", "status": status.HTTP_200_OK}

#             elif data.log_type == "error":
#                 print("ERROR hit")
#                 logger.error(data.message)
#                 return{"message": "message logged", "status": status.HTTP_200_OK}

#         elif incoming_header == "/api/website/Message":
#             logger = setup_logging("/root/logs/Website/Message", "message.log","message_log") # logger instance
#             print("Message hit")
#             if data.log_type == "info":
#                 print("INFO hit")
#                 logger.info(data.message)
#                 return{"message": "message logged", "status": status.HTTP_200_OK}

#             elif data.log_type == "warning":
#                 print("WARNING hit")
#                 logger.warning(data.message)
#                 return{"message": "message logged", "status": status.HTTP_200_OK}

#             elif data.log_type == "error":
#                 print("ERROR hit")
#                 logger.error(data.message)
#                 return{"message": "message logged", "status": status.HTTP_200_OK}

#         elif incoming_header == "/api/website/ContactUs":
#             logger = setup_logging("/root/logs/Website/ContactUs", "contactus.log","contactus_log") # logger instance
#             print("ContactUs hit")
#             if data.log_type == "info":
#                 print("INFO hit")
#                 logger.info(data.message)
#                 return{"message": "message logged", "status": status.HTTP_200_OK}

#             elif data.log_type == "warning":
#                 print("WARNING hit")
#                 logger.warning(data.message)
#                 return{"message": "message logged", "status": status.HTTP_200_OK}

#             elif data.log_type == "error":
#                 print("ERROR hit")
#                 logger.error(data.message)
#                 return{"message": "message logged", "status": status.HTTP_200_OK}
#         elif incoming_header == "/api/website/Connect":
#             logger = setup_logging("/root/logs/Website/Connect", "connect.log","connect_log")
#             print("Connect hit")
#             if data.log_type == "info":
#                 print("INFO hit")
#                 logger.info(data.message)
#                 return{"message": "message logged", "status": status.HTTP_200_OK}
#             elif data.log_type == "warning":
#                 print("WARNING hit")
#                 logger.warning(data.message)
#                 return{"message": "message logged", "status": status.HTTP_200_OK}
#             elif data.log_type == "error":
#                 print("ERROR hit")
#                 logger.error(data.message)
#                 return{"message": "message logged", "status": status.HTTP_200_OK}
#         elif incoming_header == "/api/website/Profile":
#             logger = setup_logging("/root/logs/Website/Profile", "profile.log","profile_log")
#             print("Profile hit")
#             if data.log_type == "info":
#                 print("INFO hit")
#                 logger.info(data.message)
#                 return{"message": "message logged", "status": status.HTTP_200_OK}
#             elif data.log_type == "warning":
#                 print("WARNING hit")
#                 logger.warning(data.message)
#                 return{"message": "message logged", "status": status.HTTP_200_OK}
#             elif data.log_type == "error":
#                 print("ERROR hit")
#                 logger.error(data.message)
#                 return{"message": "message logged", "status": status.HTTP_200_OK}
#         elif incoming_header == "/api/website/Patient_public_profile":
#             logger = setup_logging("/root/logs/Website/Patient_public_profile", "patient_public_profile.log","patient_public_profile_log")
#             print("Patient_public_profile hit")
#             if data.log_type == "info":
#                 print("INFO hit")
#                 logger.info(data.message)
#                 return{"message": "message logged", "status": status.HTTP_200_OK}
#             elif data.log_type == "warning":
#                 print("WARNING hit")
#                 logger.warning(data.message)
#                 return{"message": "message logged", "status": status.HTTP_200_OK}
#             elif data.log_type == "error":
#                 print("ERROR hit")
#                 logger.error(data.message)
#                 return{"message": "message logged", "status": status.HTTP_200_OK}
#         elif incoming_header == "/api/website/Doctor_public_profile":
#             logger = setup_logging("/root/logs/Website/Doctor_public_profile", "doctor_public_profile.log","doctor_public_profile_log")
#             print("Doctor_public_profile hit")
#             if data.log_type == "info":
#                 print("INFO hit")
#                 logger.info(data.message)
#                 return{"message": "message logged", "status": status.HTTP_200_OK}
#             elif data.log_type == "warning":
#                 print("WARNING hit")
#                 logger.warning(data.message)
#                 return{"message": "message logged", "status": status.HTTP_200_OK}
#             elif data.log_type == "error":
#                 print("ERROR hit")
#                 logger.error(data.message)
#                 return{"message": "message logged", "status": status.HTTP_200_OK}
#         elif incoming_header == "/api/website/Search":
#             logger = setup_logging("/root/logs/Website/Search", "search.log","search_log")
#             print("Search hit")
#             if data.log_type == "info":
#                 print("INFO hit")
#                 logger.info(data.message)
#                 return{"message": "message logged", "status": status.HTTP_200_OK}
#             elif data.log_type == "warning":
#                 print("WARNING hit")
#                 logger.warning(data.message)
#                 return{"message": "message logged", "status": status.HTTP_200_OK}
#             elif data.log_type == "error":
#                 print("ERROR hit")
#                 logger.error(data.message)
#                 return{"message": "message logged", "status": status.HTTP_200_OK}
#         elif incoming_header == "/api/website/Report_problem":
#             logger = setup_logging("/root/logs/Website/Report_problem", "report_problem.log","report_problem_log")
#             print("Report_problem hit")
#             if data.log_type == "info":
#                 print("INFO hit")
#                 logger.info(data.message)
#                 return{"message": "message logged", "status": status.HTTP_200_OK}
#             elif data.log_type == "warning":
#                 print("WARNING hit")
#                 logger.warning(data.message)
#                 return{"message": "message logged", "status": status.HTTP_200_OK}
#             elif data.log_type == "error":
#                 print("ERROR hit")
#                 logger.error(data.message)
#                 return{"message": "message logged", "status": status.HTTP_200_OK}
#         elif incoming_header == "/api/website/Img_to_json":
#             logger = setup_logging("/root/logs/Website/Img_to_json", "img_to_json.log","img_to_json_log")
#             print("Img_to_json hit")
#             if data.log_type == "info":
#                 print("INFO hit")
#                 logger.info(data.message)
#                 return{"message": "message logged", "status": status.HTTP_200_OK}
#             elif data.log_type == "warning":
#                 print("WARNING hit")
#                 logger.warning(data.message)
#                 return{"message": "message logged", "status": status.HTTP_200_OK}
#             elif data.log_type == "error":
#                 print("ERROR hit")
#                 logger.error(data.message)
#                 return{"message": "message logged", "status": status.HTTP_200_OK}
            
#         elif incoming_header == "/api/website/Pdf_to_json":
#             logger = setup_logging("/root/logs/Website/Pdf_to_json", "pdf_to_json.log","pdf_to_json_log")
#             print("Pdf_to_json hit")
#             if data.log_type == "info":
#                 print("INFO hit")
#                 logger.info(data.message)
#                 return{"message": "message logged", "status": status.HTTP_200_OK}
#             elif data.log_type == "warning":
#                 print("WARNING hit")
#                 logger.warning(data.message)
#                 return{"message": "message logged", "status": status.HTTP_200_OK}
#             elif data.log_type == "error":
#                 print("ERROR hit")
#                 logger.error(data.message)
#                 return{"message": "message logged", "status": status.HTTP_200_OK}
#         elif incoming_header == "/api/website/Timeline":
#             logger = setup_logging("/root/logs/Website/Timeline", "timeline.log","timeline_log")
#             print("Timeline hit")
#             if data.log_type == "info":
#                 print("INFO hit")
#                 logger.info(data.message)
#                 return{"message": "message logged", "status": status.HTTP_200_OK}
#             elif data.log_type == "warning":
#                 print("WARNING hit")
#                 logger.warning(data.message)
#                 return{"message": "message logged", "status": status.HTTP_200_OK}
#             elif data.log_type == "error":
#                 print("ERROR hit")
#                 logger.error(data.message)
#                 return{"message": "message logged", "status": status.HTTP_200_OK}
#     except Exception as e:
#         formatted_error = traceback.format_exc()
#         print("Error creating log: ", formatted_error)
#         logger.error(f"Error creating log: {formatted_error}")
#         return {"message": "Error creating log", "status": status.HTTP_500_INTERNAL_SERVER_ERROR}