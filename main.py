import argparse
from interfaces.cli_interface import CliInterface

# from interfaces.file_interface import FileInterface

def main():

    # Taking in user input argument with different interface choices
    parser = argparse.ArgumentParser(description="RPN calculator with multiple interfaces")
    parser.add_argument(
        "--interface",
        choices=["cli", "file"], # add more choices...
        required = True,
        help = "Choose the interface of choice (cli, file, etc)"
    )
    # parser.add_argument("--input", help="Input file path for file interface")
    # parser.add_argument("--output", help="Output file path for file interface (optional)")

    args = parser.parse_args()

    if args.interface == "cli":
        CliInterface().run()
    # elif args.interface == "file":
    #     if not args.input:
    #         print("Error: --input is required for file interface")
    #         return
    #     FileInterface(input_file=args.input, output_file=args.output).run()

if __name__ == "__main__":
    main()