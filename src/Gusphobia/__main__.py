from click import command

from .ghosts import *  # TODO: Fix imports!


@command()
def main() -> None:
    info()


if __name__ == "__main__":
    main()
