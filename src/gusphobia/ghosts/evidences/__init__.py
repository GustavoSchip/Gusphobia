"""Submodule for ghost evidence related data."""

from pydantic import BaseModel, conlist


class Evidence(BaseModel):
    name: str
    description: str


EMF5: Evidence = Evidence(
    name="EMF 5",
    description="Some Ghosts leave Electro Magnetic Fields (EMF) when they interact with things. Look out for extra strong readings that reach level 5.",
)
UltraViolet: Evidence = Evidence(
    name="Ultraviolet",
    description="Some Ghosts have been known to leave fingerprints on objects such as doors and light switches, as well as leaving footprints after stepping in Salt. These can be revealed with a UV Light.",
)
WritingBook: Evidence = Evidence(
    name="Written Book",
    description="Some Ghosts are able to write inside of books if given the proper tools to do so.",
)
Freezing: Evidence = Evidence(
    name="Freezing",
    description="All ghosts make rooms cold, however, some have been known to make the temperature drop extremely fast.",
)
DOTS: Evidence = Evidence(
    name="D.O.T.S.",
    description="A laser grid of light that can reveal the silhouette of the ghost.",
)
GhostOrbs: Evidence = Evidence(
    name="Ghost Orbs",
    description="Small floating orbs of light, only visible through a camera.",
)
SpiritBox: Evidence = Evidence(
    name="Spirit Box",
    description="Only certain ghosts will talk through a Spirit Box when asked a question with your voice. Make sure the lights are turned off.",
)
Evidences: conlist(Evidence, min_length=7, max_length=7) = [
    EMF5,
    UltraViolet,
    WritingBook,
    Freezing,
    DOTS,
    GhostOrbs,
    SpiritBox,
]


__all__ = [
    "Evidence",
    "Evidences",
    "EMF5",
    "UltraViolet",
    "WritingBook",
    "Freezing",
    "DOTS",
    "GhostOrbs",
    "SpiritBox",
]
