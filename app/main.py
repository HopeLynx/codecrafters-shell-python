import sys


def main():
    command_list = ["exit 0"]
    # Wait for user input
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        command = input()
        if command not in command_list:
            sys.stdout.write(f"{command}: command not found\n")
        elif command == command_list[0]:
            return 0
            

if __name__ == "__main__":
    main()
