from app.repositories.concept_repository import get_all_concepts

def list_concepts(db):
    return get_all_concepts(db)