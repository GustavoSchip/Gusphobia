from typing import Optional

from ...ghosts import ghost_variations
from ...ghosts.evidences import evidence_variations


def normalize_evidence(evidence: str) -> str:
    return evidence.lower().replace(" ", "")


def detect_evidence(evidence: str) -> Optional[str]:
    normalized_evidence: str = normalize_evidence(evidence)
    for key, variations in evidence_variations.items():
        if normalized_evidence in variations:
            return key
    return None


def normalize_ghost(ghost_name: str) -> str:
    return ghost_name.lower().replace(" ", "")


def detect_ghost(ghost_name: str) -> Optional[str]:
    normalized_ghost: str = normalize_ghost(ghost_name)
    for key, variations in ghost_variations.items():
        if normalized_ghost in variations:
            return key
    return None


__all__ = ["normalize_evidence", "detect_evidence", "normalize_ghost", "detect_ghost"]
