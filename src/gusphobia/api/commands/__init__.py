"""Submodule for api command related data."""

from typing import List, Optional

from click import secho, style

from .helper import normalize_evidence, detect_evidence, normalize_ghost, detect_ghost
from ..ghosts import ghost_map, identify_ghost, possible_ghosts
from ..ghosts.evidences import evidence_map
from ...ghosts import Ghost
from ...ghosts.evidences import Evidence


def evidence(evidences: List[str]) -> None:
    secho("")

    if not evidences or len(evidences) < 1:
        secho("Please provide at least one evidence.", fg="red", bold=True)
        secho("")
        return

    evidence_objects: List[Evidence] = []
    parsed_evidences: list[Optional[str]] = []
    for _evidence in evidences:
        detected_evidence: Optional[str] = detect_evidence(_evidence)
        if detected_evidence and detected_evidence in evidence_map:
            evidence_objects.append(evidence_map[detected_evidence])
            parsed_evidences.append(detected_evidence)
        else:
            secho(f"Invalid evidence: {_evidence}", fg="red", bold=True)
            secho("")
            return

    secho(f"Parsed evidences: {', '.join(parsed_evidences)}", fg="magenta")

    if len(evidence_objects) == 3:
        identified_ghost: Optional[Ghost] = identify_ghost(evidence_objects)
        if identified_ghost:
            secho("")
            secho(f"{style('Ghost', fg='yellow')}: {identified_ghost.name}")
            secho(f"{style('Description', fg='blue')}: {identified_ghost.description}")
            secho(
                f"{style('Ability', fg='green')}: {identified_ghost.ability.description}"
            )
            secho(f"{style('Sanity', fg='red')}: {identified_ghost.hunt_range}")
            secho("")
        else:
            secho("No ghost matches all the given evidence.", fg="red", bold=True)
            secho("")
            return
    else:
        secho("Possible ghosts based on the given evidence are:", fg="magenta")
        secho("")
        for __ghost in possible_ghosts(evidence_objects):
            secho(f"{style('Ghost', fg='yellow')}: {__ghost.name}")
            secho(
                f"{style('Evidences', fg='cyan')}: {', '.join([__evidence.name for __evidence in __ghost.evidences])}"
            )
            secho(f"{style('Ability', fg='green')}: {__ghost.ability.description}")
            secho(f"{style('Sanity', fg='red')}: {__ghost.hunt_range}")
            secho("")
    return


def ghost(name: str) -> None:
    secho("")

    if not name:
        secho("Please provide a ghost.", fg="red", bold=True)
        secho("")
        return

    detected_ghost: Optional[str] = detect_ghost(name)
    if detected_ghost and detected_ghost in ghost_map:
        __ghost: Ghost = ghost_map[detected_ghost]
        secho(f"Parsed ghost: {__ghost.name}", fg="magenta")
        secho("")

        secho(f"{style('Ghost', fg='yellow')}: {__ghost.name}")
        secho(f"{style('Description', fg='blue')}: {__ghost.description}")
        secho(
            f"{style('Evidences', fg='cyan')}: {', '.join([__evidence.name for __evidence in __ghost.evidences])}"
        )
        secho(f"{style('Ability', fg='green')}: {__ghost.ability.description}")
        secho(f"{style('Sanity', fg='red')}: {__ghost.hunt_range}")
        secho("")
    else:
        secho(f"Invalid ghost: {name}", fg="red", bold=True)
        secho("")
        return
    return


__all__ = ["evidence", "ghost"]
