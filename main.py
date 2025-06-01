import argparse
from interfaces.cli_interface import CliInterface

def main():

    # Taking in user input argument with different interface choices
    parser = argparse.ArgumentParser(description="RPN calculator with multiple interfaces")
    parser.add_argument(
        "--interface",
        choices=["cli", "websocket"], # add more choices...
        required = True,
        help = "Choose the interface of choice (cli, websocket, etc)"
    )

    args = parser.parse_args()

    if args.interface == "cli":
        CliInterface().run()

if __name__ == "__main__":
    main()