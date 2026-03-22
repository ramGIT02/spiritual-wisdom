from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.practice import Practice
from app.schemas.practice import PracticeOut

router = APIRouter(prefix="/practices", tags=["practices"])


@router.get("", response_model=list[PracticeOut])
def list_practices(db: Session = Depends(get_db)):
    return db.query(Practice).order_by(Practice.name.asc()).all()


@router.get("/{practice_id}", response_model=PracticeOut)
def get_practice(practice_id: int, db: Session = Depends(get_db)):
    practice = db.query(Practice).filter(Practice.id == practice_id).first()
    if not practice:
        raise HTTPException(status_code=404, detail="Practice not found")
    return practice
