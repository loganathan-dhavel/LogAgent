from pydantic import BaseModel, Field
from enum import Enum
from datetime import datetime

class ModelName(str,Enum):
    MISTRAL_7B = "mistral:7b"

class QueryInput(BaseModel):
    question: str
    session_id: str = Field(default=None, description="Session ID for the chat session")
    model: ModelName = Field(default=ModelName.MISTRAL_7B, description="Model to use for the query")

class QueryResponse(BaseModel):
    answer: str
    session_id: str
    model: ModelName

class DocumentInfo(BaseModel):
    id: int
    filename: str
    upload_timestamp: datetime

class DeleteFileRequest(BaseModel):
    file_id: int