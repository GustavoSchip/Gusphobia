from typing import List

from click import echo

from ..ghosts import identify_ghost, possible_ghosts
from ..ghosts.evidences import evidence_map


def evidence(evidences: List[str]) -> None:
    if not evidences or len(evidences) < 1:
        echo("Please provide at least one evidence.")
        return

    evidence_objects = []
    for _evidence in evidences:
        if _evidence in evidence_map:
            evidence_objects.append(evidence_map[_evidence])
        else:
            echo(f"Invalid evidence: {_evidence}")
            return

    identified_ghost = identify_ghost(evidence_objects)
    if identified_ghost:
        echo(f"The ghost is: {identified_ghost.name}")
    else:
        echo("No ghost matches all the given evidence. Possible ghosts are:")
        for ghost in possible_ghosts(evidences):
            echo(ghost.name)


__all__ = ["evidence"]
