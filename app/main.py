import sys


def main():
    sys.stdout.write("$ ")
    sys.stdout.flush()
    command_list = []
    # Wait for user input
    while True:
        command = input()
        if command not in command_list:
            sys.stdout.write(f"{command}: command not found\n")

if __name__ == "__main__":
    main()
