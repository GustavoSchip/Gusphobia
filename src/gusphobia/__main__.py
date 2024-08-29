"""My program for use with the Phasmophobia video game."""

from sys import argv
from typing import List

from click import argument, group

from .api.commands import evidence


@group()
def cli() -> None:
    pass


@cli.command(name="evidence")
@argument("evidences", nargs=-1)
def _evidence(evidences: List[str]) -> None:
    return evidence(evidences)


if __name__ == "__main__":
    if len(argv) == 1:
        cli(["--help"])
    else:
        cli()
