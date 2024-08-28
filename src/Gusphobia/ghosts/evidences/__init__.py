from pydantic import BaseModel


class Evidence(BaseModel):
    name: str
    description: str
