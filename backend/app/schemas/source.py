from pydantic import BaseModel


class SourceOut(BaseModel):
    id: int
    title: str
    tradition: str
    source_type: str
    description: str
    chapters_count: int

    model_config = {"from_attributes": True}


class ChapterOut(BaseModel):
    id: int
    source_id: int
    chapter_number: int
    title: str

    model_config = {"from_attributes": True}
