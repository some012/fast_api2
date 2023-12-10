from pydantic import BaseModel, Field

class User(BaseModel):
    id: int = Field(gt=0)
    name: str = Field(max_length=45)
    phone: str = Field(max_length=20, pattern=r'[0-9*#+]+$')
    passport: str = Field(max_length=15, min_length=9, pattern=r'^\d*$')