import sys
import os


def main():
    command_list = ["exit","echo","type"]
    # Wait for user input
    PATH = os.environ.get("PATH")
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
            cmd_path = None
            paths = PATH.split(":")
            for path in paths:
                if os.path.exists(f"{path}/{splitted_command[1]}"):
                    cmd_path = f"{path}/{splitted_command[1]}"
            if cmd_path:
                sys.stdout.write(f"{splitted_command[1]} is {cmd_path}\n")
            elif splitted_command[1] in command_list:
                sys.stdout.write(f"{splitted_command[1]} is a shell builtin\n")
            else:
                sys.stdout.write(f"{splitted_command[1]} not found\n")

            

if __name__ == "__main__":
    main()
