from app.models.concept import Concept

def get_all_concepts(db):
    return db.query(Concept).all()