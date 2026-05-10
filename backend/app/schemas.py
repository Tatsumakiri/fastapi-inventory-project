
from pydantic import BaseModel, Field

class ItemCreate(BaseModel):
    name: str = Field(min_length=1, max_length=50)
    quantity: int = Field(ge=0)



class ItemResponse(BaseModel):
    id: int
    name: str
    quantity: int

    class Config:
        from_attributes = True