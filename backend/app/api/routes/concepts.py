from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.services.concepts_service import list_concepts

router = APIRouter(prefix="/concepts", tags=["concepts"])

@router.get("")
def get_concepts(db: Session = Depends(get_db)):
    return list_concepts(db)