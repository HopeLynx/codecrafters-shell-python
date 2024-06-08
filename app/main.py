import sys


def main():
    sys.stdout.write("$ ")
    sys.stdout.flush()
    command_list = []
    # Wait for user input
    command = input()
    if command not in command_list:
        sys.stdout.write("{command}: command not found")

if __name__ == "__main__":
    main()
