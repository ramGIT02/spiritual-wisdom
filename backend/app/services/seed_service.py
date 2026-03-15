import json
from pathlib import Path

from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.models.chapter import Chapter
from app.models.concept import Concept
from app.models.practice import Practice
from app.models.source import Source
from app.models.verse import Verse

BASE_DIR = Path(__file__).resolve().parents[1]
SEED_DIR = BASE_DIR / "seed"


def load_json(filename: str):
    with open(SEED_DIR / filename, "r", encoding="utf-8") as f:
        return json.load(f)


def seed_items(db: Session, model, filename: str):
    for item in load_json(filename):
        if not db.query(model).filter(model.id == item["id"]).first():
            db.add(model(**item))
    db.commit()


def run_seed():
    db = SessionLocal()
    try:
        seed_items(db, Source, "sources.json")
        seed_items(db, Chapter, "chapters.json")
        seed_items(db, Verse, "verses.json")
        seed_items(db, Concept, "concepts.json")
        seed_items(db, Practice, "practices.json")
        print("Seeding complete.")
    finally:
        db.close()


if __name__ == "__main__":
    run_seed()
