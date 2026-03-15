from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.chapter import Chapter
from app.models.source import Source
from app.schemas.source import ChapterOut, SourceOut

router = APIRouter(prefix="/sources", tags=["sources"])


@router.get("", response_model=list[SourceOut])
def list_sources(db: Session = Depends(get_db)):
    return db.query(Source).order_by(Source.title.asc()).all()


@router.get("/{source_id}", response_model=SourceOut)
def get_source(source_id: int, db: Session = Depends(get_db)):
    item = db.query(Source).filter(Source.id == source_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Source not found")
    return item


@router.get("/{source_id}/chapters", response_model=list[ChapterOut])
def list_source_chapters(source_id: int, db: Session = Depends(get_db)):
    source = db.query(Source).filter(Source.id == source_id).first()
    if not source:
        raise HTTPException(status_code=404, detail="Source not found")
    return db.query(Chapter).filter(Chapter.source_id == source_id).order_by(Chapter.chapter_number.asc()).all()
