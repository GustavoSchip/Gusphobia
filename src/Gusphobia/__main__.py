from click import command, echo


@command()
def main() -> None:
    echo("TEST")  # TODO


if __name__ == "__main__":
    main()
