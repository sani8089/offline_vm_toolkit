import argparse

from . import __version__


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Offline VM Toolkit")
    subparsers = parser.add_subparsers(dest="command", required=True)

    greet_parser = subparsers.add_parser("greet", help="Greet someone")
    greet_parser.add_argument("name", help="Name to greet")

    subparsers.add_parser("version", help="Show version")

    return parser


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command == "greet":
        print(f"Hello, {args.name}!")
    elif args.command == "version":
        print(__version__)


if __name__ == "__main__":
    main()
