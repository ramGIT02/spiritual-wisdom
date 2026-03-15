from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.models.concept import Concept
from app.models.content_chunk import ContentChunk
from app.models.content_embedding import ContentEmbedding
from app.models.verse import Verse
from app.services.embedding_service import create_embedding


def rebuild_chunks(db: Session):
    db.query(ContentEmbedding).delete()
    db.query(ContentChunk).delete()
    db.commit()

    verses = db.query(Verse).all()
    for verse in verses:
        content = (
            f"Reference: {verse.canonical_reference}\n"
            f"Translation: {verse.translation}\n"
            f"Explanation: {verse.explanation}\n"
            f"Life Application: {verse.life_application}"
        )
        chunk = ContentChunk(
            entity_type="verse",
            entity_id=verse.id,
            source_label=verse.canonical_reference,
            title=verse.canonical_reference,
            content=content,
            metadata_json={},
        )
        db.add(chunk)
        db.flush()
        db.add(ContentEmbedding(chunk_id=chunk.id, embedding=create_embedding(content)))

    concepts = db.query(Concept).all()
    for concept in concepts:
        content = (
            f"Concept: {concept.name}\n"
            f"Short Definition: {concept.short_definition}\n"
            f"Detailed Explanation: {concept.detailed_explanation}"
        )
        chunk = ContentChunk(
            entity_type="concept",
            entity_id=concept.id,
            source_label=concept.name,
            title=concept.name,
            content=content,
            metadata_json={"related_concepts": [concept.name]},
        )
        db.add(chunk)
        db.flush()
        db.add(ContentEmbedding(chunk_id=chunk.id, embedding=create_embedding(content)))

    db.commit()


if __name__ == "__main__":
    db = SessionLocal()
    try:
        rebuild_chunks(db)
        print("Chunks and embeddings rebuilt.")
    finally:
        db.close()
