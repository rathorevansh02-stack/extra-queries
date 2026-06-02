import sys

def show_help():
    print("Standard Student CLI Tool")
    print("Usage: python cli_tool.py [command] [arguments]")
    print("\nAvailable Commands:")
    print("  help              Shows this help manual menu")
    print("  greet [name]      Prints a clean text greeting for the specified name")
    print("  square [number]   Calculates and returns the square of a given number")

def main():
    # sys.argv captures everything typed in the terminal command line string.
    # sys.argv[0] is always the name of the file itself ('cli_tool.py')
    arguments = sys.argv[1:]

    # If the user typed no commands, show the help manual
    if not arguments:
        show_help()
        return

    # Extract the primary command word
    command = arguments[0].lower()

    if command == "help":
        show_help()

    elif command == "greet":
        # Check if the user provided the required name argument
        if len(arguments) < 2:
            print("Error: The 'greet' command requires a name argument.")
            print("Example: python cli_tool.py greet Rudra")
        else:
            name = arguments[1]
            print(f"Hello, {name}! Your custom CLI pipeline is working perfectly.")

    elif command == "square":
        # Check if the user provided the required number argument
        if len(arguments) < 2:
            print("Error: The 'square' command requires a number argument.")
            print("Example: python cli_tool.py square 5")
        else:
            try:
                number = int(arguments[1])
                print(f"The square of {number} is: {number * number}")
            except ValueError:
                print("Error: Please provide a valid integer value to square.")

    else:
        print(f"Unknown command instruction: '{command}'")
        print("Type 'python cli_tool.py help' to view valid options.")

if __name__ == "__main__":
    main()