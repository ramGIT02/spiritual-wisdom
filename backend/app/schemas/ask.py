from pydantic import BaseModel, Field


class AskRequest(BaseModel):
    question: str = Field(min_length=3, max_length=1000)
    mode: str = Field(default="simple")


class AskResponse(BaseModel):
    answer: str
    sources: list[str]
    related_concepts: list[str]
    suggested_practice: str | None = None
    disclaimer: str
