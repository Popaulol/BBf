import argparse


def main() -> None:

    parser = argparse.ArgumentParser(
        description="The official Interpreter for the BBf (Better Brainfuck) language"
    )
    parser.add_argument(
        "FILE",
    )

    file = parser.parse_args().file


if __name__ == "__main__":
    main()
