"""My program for use with the Phasmophobia video game."""

from sys import argv
from typing import List

from click import argument, group

from .api.commands import evidence, ghost


@group()
def cli() -> None:
    """My program for use with the Phasmophobia video game."""
    """Placeholder for command tree/group."""
    pass


@cli.command(name="evidence")
@argument("evidences", nargs=-1)
def _evidence(evidences: List[str]) -> None:
    """Supply the evidences gathered to list all possible ghost"""
    """Proxy handle to reduce clutter."""
    return evidence(evidences)


@cli.command(name="ghost")
@argument("name")
def _ghost(name: str) -> None:
    """Supply the name of a ghost to see info about that ghost."""
    """Proxy handle to reduce clutter."""
    return ghost(name)


if __name__ == "__main__":
    """Entrypoint."""
    if len(argv) == 1:
        """If no arguments are given then display the 'help' menu."""
        cli(["--help"])
    else:
        cli()
