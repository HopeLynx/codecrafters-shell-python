import sys


def main():
    command_list = ["exit","echo","type"]
    # Wait for user input
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        command = input()
        splitted_command = command.split()
        if splitted_command[0] not in command_list:
            sys.stdout.write(f"{splitted_command[0]}: command not found\n")
        elif splitted_command[0] == command_list[0]:
            return 0
        elif splitted_command[0] == command_list[1]:
            sys.stdout.write(f"{" ".join(splitted_command[1:])}\n")
        elif splitted_command[0] == command_list[2]:
            if splitted_command[1] not in command_list:
                sys.stdout.write(f"{splitted_command[1]} not found\n")
            else:
                sys.stdout.write(f"{splitted_command[1]} is a shell builtin\n")

            

if __name__ == "__main__":
    main()
