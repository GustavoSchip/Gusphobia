from sys import argv
from typing import List

from click import argument, echo, group

from .api import evidence_map, identify_ghost, possible_ghosts


@group()
def cli() -> None:
    pass


@cli.command()
@argument("evidences", nargs=-1)
def evidence(evidences: List[str]) -> None:
    if not evidences or len(evidences) < 1:
        echo("Please provide at least one evidence.")
        return

    evidence_objects = []
    for evidence in evidences:
        if evidence in evidence_map:
            evidence_objects.append(evidence_map[evidence])
        else:
            echo(f"Invalid evidence: {evidence}")
            return

    identified_ghost = identify_ghost(evidence_objects)
    if identified_ghost:
        echo(f"The ghost is: {identified_ghost.name}")
    else:
        echo("No ghost matches all the given evidence. Possible ghosts are:")
        for ghost in possible_ghosts(evidences):
            echo(ghost.name)


if __name__ == "__main__":
    if len(argv) == 1:
        cli(["--help"])
    else:
        cli()
