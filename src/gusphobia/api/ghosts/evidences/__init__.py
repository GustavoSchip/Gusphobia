"""Submodule for api ghost evidence related data."""

from ....ghosts.evidences import (
    Evidence,
    EMF5,
    UltraViolet,
    WritingBook,
    Freezing,
    DOTS,
    GhostOrbs,
    SpiritBox,
)


evidence_map: dict[str, Evidence] = {
    "EMF5": EMF5,
    "UltraViolet": UltraViolet,
    "WritingBook": WritingBook,
    "Freezing": Freezing,
    "DOTS": DOTS,
    "GhostOrbs": GhostOrbs,
    "SpiritBox": SpiritBox,
}
evidence_variations: dict[str, list[str]] = (
    {  # TODO: Remove unnecessary " " characters.
        "EMF5": ["emf5", "emf", "emf 5", "emf-5"],
        "UltraViolet": ["ultraviolet", "uv", "uvlight", "uv light"],
        "WritingBook": [
            "writingbook",
            "book",
            "writing book",
            "ghostwriting",
            "ghost writing",
        ],
        "Freezing": [
            "freezing",
            "temp",
            "freezingtemps",
            "freezing temps",
            "freezingtemperatures",
            "freezing temperatures",
        ],
        "DOTS": ["dots", "dotsprojector", "dots projector"],
        "GhostOrbs": ["ghostorbs", "orbs", "ghost orbs"],
        "SpiritBox": ["spiritbox", "box", "spirit box"],
    }
)


__all__ = ["evidence_map", "evidence_variations"]
