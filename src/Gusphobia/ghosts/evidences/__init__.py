from pydantic import BaseModel


class Evidence(BaseModel):
    name: str
    description: str  # TODO


EMF5 = Evidence(name="EMF 5", description="")
UltraViolet = Evidence(name="Ultraviolet", description="")
WritingBook = Evidence(name="Written Book", description="")
Freezing = Evidence(name="Freezing", description="")
DOTS = Evidence(name="D.O.T.S.", description="")
GhostOrbs = Evidence(name="Ghost Orbs", description="")
SpiritBox = Evidence(name="Spirit Box", description="")


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
