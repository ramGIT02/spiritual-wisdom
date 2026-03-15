from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import or_
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.concept import Concept
from app.schemas.concept import ConceptOut

router = APIRouter(prefix="/concepts", tags=["concepts"])


@router.get("", response_model=list[ConceptOut])
def list_concepts(q: str | None = Query(default=None), db: Session = Depends(get_db)):
    query = db.query(Concept)
    if q:
        pattern = f"%{q}%"
        query = query.filter(
            or_(
                Concept.name.ilike(pattern),
                Concept.short_definition.ilike(pattern),
                Concept.detailed_explanation.ilike(pattern),
            )
        )
    return query.order_by(Concept.name.asc()).all()


@router.get("/{concept_id}", response_model=ConceptOut)
def get_concept(concept_id: int, db: Session = Depends(get_db)):
    concept = db.query(Concept).filter(Concept.id == concept_id).first()
    if not concept:
        raise HTTPException(status_code=404, detail="Concept not found")
    return concept
