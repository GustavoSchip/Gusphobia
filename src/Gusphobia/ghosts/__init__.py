from typing import Union, List

from pydantic import BaseModel

from .abilities import Ability
from .evidences import Evidence


class Ghost(BaseModel):
    name: str
    description: str
    hunt_range: Union[str, int]
    ability: Ability
    evidences: List[Evidence, Evidence, Evidence]
