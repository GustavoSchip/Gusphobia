from click import command

from .api import info


@command()
def main() -> None:
    info()


if __name__ == "__main__":
    main()
