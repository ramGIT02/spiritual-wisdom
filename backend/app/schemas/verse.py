from pydantic import BaseModel


class VerseSummaryOut(BaseModel):
    id: int
    source_id: int
    chapter_id: int
    chapter_number: int
    verse_number: int
    canonical_reference: str
    translation: str

    model_config = {"from_attributes": True}


class VerseOut(BaseModel):
    id: int
    source_id: int
    chapter_id: int
    chapter_number: int
    verse_number: int
    canonical_reference: str
    sanskrit: str
    transliteration: str
    translation: str
    explanation: str
    life_application: str

    model_config = {"from_attributes": True}
