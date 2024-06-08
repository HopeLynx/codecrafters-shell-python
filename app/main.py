import sys
import os

PATH = os.environ["PATH"].split(":")

def _find_exec(name):
    for dir in PATH:
        path = os.path.join(dir, name)
        if os.path.exists(path):
            return path
    else:
        return None

def main():
    command_list = ["exit","echo","type","pwd","cd"]
    # Wait for user input
    # PATH = os.environ.get("PATH")
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        command = input()
        splitted_command = command.split()
        
        if splitted_command[0] == command_list[0]:
            return 0
        elif splitted_command[0] == command_list[1]:
            sys.stdout.write(f"{" ".join(splitted_command[1:])}\n")
        elif splitted_command[0] == command_list[2]:
            cmd_path = None
            paths = PATH
            for path in paths:
                if os.path.exists(f"{path}/{splitted_command[1]}"):
                    cmd_path = f"{path}/{splitted_command[1]}"

            if splitted_command[1] in command_list:
                sys.stdout.write(f"{splitted_command[1]} is a shell builtin\n")
            elif cmd_path:
                sys.stdout.write(f"{splitted_command[1]} is {cmd_path}\n")
            else:
                sys.stdout.write(f"{splitted_command[1]} not found\n")
        elif splitted_command[0] == command_list[3]:
            sys.stdout.write(f"{os.getcwd()}\n")
        elif splitted_command[0] == command_list[4]:
            if os.path.exists(os.path.expanduser(splitted_command[1])):
                os.chdir(os.path.expanduser(splitted_command[1]))
            else:
                sys.stdout.write(f"{splitted_command[1]}: No such file or directory\n")
        else:
            if path := _find_exec(splitted_command[0]):
                exitcode = os.spawnv(os.P_WAIT, path, splitted_command)
            else:
                sys.stdout.write(f"{splitted_command[0]}: command not found\n")
                    

if __name__ == "__main__":
    main()
