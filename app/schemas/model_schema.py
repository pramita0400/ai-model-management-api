from pydantic import BaseModel
from typing import Optional

class ModelCreate(BaseModel):
    name:str
    version:str
    description:Optional[str]=None 
    framework:str # e.g. "pytorch", "sklearn", "tensorflow"
class ModelResponse(BaseModel):
    id:int
    name:str
    version:str
    description:Optional[str]=None
    framework:str

