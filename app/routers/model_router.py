from fastapi import APIRouter
from app.schemas.model_schema import ModelCreate,ModelResponse

router=APIRouter(prefix="/models",tags=["Models"])

@router.get("/")
def list_models():
    return {"models":[]}

@router.post("/",response_model=ModelResponse)
def register_model(model:ModelCreate):
    return {**model.model_dump(),"id":1}

