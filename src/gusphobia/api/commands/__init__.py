from typing import List

from click import echo

from .helper import normalize_evidence, detect_evidence
from ..ghosts import identify_ghost, possible_ghosts
from ..ghosts.evidences import evidence_map


def evidence(evidences: List[str]) -> None:
    if not evidences or len(evidences) < 1:
        echo("Please provide at least one evidence.")
        return

    evidence_objects = []
    parsed_evidences = []
    for _evidence in evidences:
        detected_evidence = detect_evidence(_evidence)
        if detected_evidence and detected_evidence in evidence_map:
            evidence_objects.append(evidence_map[detected_evidence])
            parsed_evidences.append(detected_evidence)
        else:
            echo(f"Invalid evidence: {_evidence}")
            return

    echo(f"Parsed evidences: {', '.join(parsed_evidences)}")

    if len(evidence_objects) == 3:
        identified_ghost = identify_ghost(evidence_objects)
        if identified_ghost:
            echo(f"The ghost is: {identified_ghost.name}")
        else:
            echo("No ghost matches all the given evidence.")
    else:
        echo("Possible ghosts based on the given evidence are:")
        for ghost in possible_ghosts(evidence_objects):
            echo(ghost.name)


__all__ = ["evidence"]
