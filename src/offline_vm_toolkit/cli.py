import argparse


def hello(args: argparse.Namespace) -> None:
    """Print a friendly greeting."""
    name = args.name
    print(f"Hello, {name}!")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Offline VM Toolkit CLI")
    subparsers = parser.add_subparsers(dest="command")

    hello_parser = subparsers.add_parser("hello", help="Say hello")
    hello_parser.add_argument("--name", default="world", help="Name to greet")
    hello_parser.set_defaults(func=hello)

    return parser


def main(argv: list[str] | None = None) -> None:
    parser = build_parser()
    args = parser.parse_args(argv)
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
