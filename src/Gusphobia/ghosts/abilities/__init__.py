from pydantic import BaseModel


class Ability(BaseModel):
    name: str
    description: str
