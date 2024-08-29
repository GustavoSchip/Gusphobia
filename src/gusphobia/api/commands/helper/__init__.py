from typing import Optional

from ...ghosts.evidences import evidence_variations


def normalize_evidence(evidence: str) -> str:
    return evidence.lower().replace(" ", "")


def detect_evidence(evidence: str) -> Optional[str]:
    normalized_evidence = normalize_evidence(evidence)
    for key, variations in evidence_variations.items():
        if normalized_evidence in variations:
            return key
    return None


__all__ = ["normalize_evidence", "detect_evidence"]
