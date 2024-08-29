from ....ghosts.evidences import (
    EMF5,
    UltraViolet,
    WritingBook,
    Freezing,
    DOTS,
    GhostOrbs,
    SpiritBox,
)


evidence_map = {
    "EMF5": EMF5,
    "UltraViolet": UltraViolet,
    "WritingBook": WritingBook,
    "Freezing": Freezing,
    "DOTS": DOTS,
    "GhostOrbs": GhostOrbs,
    "SpiritBox": SpiritBox,
}
evidence_variations = {
    "EMF5": ["emf5", "emf 5", "emf-5"],
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
        "freezingtemps",
        "freezing temps",
        "freezingtemperatures",
        "freezing temperatures",
    ],
    "DOTS": ["dots", "dotsprojector", "dots projector"],
    "GhostOrbs": ["ghostorbs", "orbs", "ghost orbs"],
    "SpiritBox": ["spiritbox", "box", "spirit box", "spiritbox"],
}


__all__ = ["evidence_map", "evidence_variations"]
