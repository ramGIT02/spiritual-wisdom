from pydantic import BaseModel


class PracticeOut(BaseModel):
    id: int
    name: str
    tradition: str
    duration_minutes: int
    purpose: str
    benefits: str
    common_mistakes: str

    model_config = {"from_attributes": True}
