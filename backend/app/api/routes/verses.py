from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import or_
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.verse import Verse
from app.schemas.verse import VerseOut, VerseSummaryOut

router = APIRouter(tags=["verses"])


@router.get("/chapters/{chapter_id}/verses", response_model=list[VerseSummaryOut])
def list_verses(chapter_id: int, db: Session = Depends(get_db)):
    return db.query(Verse).filter(Verse.chapter_id == chapter_id).order_by(Verse.verse_number.asc()).all()


@router.get("/verses/{verse_id}", response_model=VerseOut)
def get_verse(verse_id: int, db: Session = Depends(get_db)):
    verse = db.query(Verse).filter(Verse.id == verse_id).first()
    if not verse:
        raise HTTPException(status_code=404, detail="Verse not found")
    return verse


@router.get("/verses/search", response_model=list[VerseSummaryOut])
def search_verses(q: str = Query(..., min_length=2), db: Session = Depends(get_db)):
    pattern = f"%{q}%"
    return (
        db.query(Verse)
        .filter(
            or_(
                Verse.canonical_reference.ilike(pattern),
                Verse.translation.ilike(pattern),
                Verse.explanation.ilike(pattern),
                Verse.life_application.ilike(pattern),
            )
        )
        .order_by(Verse.chapter_number.asc(), Verse.verse_number.asc())
        .all()
    )
