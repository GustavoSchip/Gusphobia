from pydantic import BaseModel


class Evidence(BaseModel):
    name: str


EMF5 = Evidence(name="EMF 5")
UltraViolet = Evidence(name="Ultraviolet")
WritingBook = Evidence(name="Written Book")
Freezing = Evidence(name="Freezing")
DOTS = Evidence(name="D.O.T.S.")
GhostOrbs = Evidence(name="Ghost Orbs")
SpiritBox = Evidence(name="Spirit Box")


__all__ = [
    "Evidence",
    "EMF5",
    "UltraViolet",
    "WritingBook",
    "Freezing",
    "DOTS",
    "GhostOrbs",
    "SpiritBox",
]
