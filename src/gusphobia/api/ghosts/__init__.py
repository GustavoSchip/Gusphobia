from typing import List, Optional

from ...ghosts import Ghost, Ghosts


def identify_ghost(evidences: List[str]) -> Optional[Ghost]:
    for ghost in Ghosts:
        if all(evidence in ghost.evidences for evidence in evidences):
            return ghost
    return None


def possible_ghosts(evidences: List[str]) -> List[Ghost]:
    possible = []
    for ghost in Ghosts:
        if any(evidence in ghost.evidences for evidence in evidences):
            possible.append(ghost)
    return possible


__all__ = ["identify_ghost", "possible_ghosts"]
