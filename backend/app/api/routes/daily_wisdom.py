from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.verse import Verse

router = APIRouter(prefix="/daily-wisdom", tags=["daily-wisdom"])


@router.get("")
def get_daily_wisdom(db: Session = Depends(get_db)):
    try:
        verse = db.query(Verse).filter(Verse.canonical_reference == "Bhagavad Gita 2.47").first()

        if not verse:
            return {
                "reference": "Bhagavad Gita 2.47",
                "text": "You have a right to action alone, never to its fruits.",
                "explanation": "A practical teaching on sincere effort without bondage to outcome.",
                "reflection_prompt": "What can you do today with full sincerity and less anxiety about the result?",
            }

        return {
            "reference": verse.canonical_reference,
            "text": verse.translation,
            "explanation": verse.explanation,
            "reflection_prompt": "Where can you act today with sincerity and less attachment to outcome?",
        }
    except Exception as e:
        return {
            "reference": "debug",
            "text": "debug",
            "explanation": str(e),
            "reflection_prompt": "debug",
        }