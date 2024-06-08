import sys


def main():
    sys.stdout.write("$ ")
    sys.stdout.flush()
    command_list = []
    # Wait for user input
    command = input()

    while command:
        if command not in command_list:
            sys.stdout.write(f"{command}: command not found\n")
        command = input()

if __name__ == "__main__":
    main()
