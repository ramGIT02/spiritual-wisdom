from pydantic import BaseModel


class ConceptOut(BaseModel):
    id: int
    name: str
    short_definition: str
    detailed_explanation: str

    model_config = {"from_attributes": True}
