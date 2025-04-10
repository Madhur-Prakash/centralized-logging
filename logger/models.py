from pydantic import BaseModel, Field

class newlog(BaseModel):
    log_type: str = Field(..., title="type of log")
    message: str = Field(..., title="message for logging")