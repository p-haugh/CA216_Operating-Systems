import os
import getpass
import socket
import pathlib
import sys
import readline

sesh_file = os.getcwd() + "/" + sys.argv[0]

def make_completer(vocab):
    def custom_complete(text, state):
        results = [x for x in vocab if x.startswith(text)] + [None]
        return results[state] + " "
    return custom_complete

def main():
    readline.parse_and_bind("tab: complete")
    while True:
        USER = getpass.getuser()
        HOST = socket.gethostname()
        PWD = os.getcwd()
        readline.set_completer(make_completer(os.listdir(".")))
        line  = read_line(USER, HOST, PWD)
        args = tokenize(line)
        execute(args)

def read_line(USER, HOST, PWD):
    line  = input("\n" + USER + " in " + HOST + " at " + PWD + " > ").strip()
    return line

def tokenize(line):
    args = line.split()
    return args

def launch(args):
    pid = os.fork()
    if pid > 0:
        wpid = os.waitpid(pid, 0)
    else:
        try:
            os.execvp(args[0], args)
        except Exception as e:
            print("sesh: command not found: " + args[0])

def execute(args):
    try:
        if len(args) == 0:
            pass
        elif 'cd' == args[0]:
            cd("".join(args[1:]))
        elif 'quit' == args[0]:
            quit()
        elif "sesh" == args[0]:
            sesh("".join(args[1:]))
        else:
            launch(args)
    except EOFError as e:
        print (" ")

def sesh(args):
    try:
        for line in open(args, "r"):
            execute(line.split())
    except Exception as e:
        print("sesh: cannot access " + args + ": No such file or directory")

def cd(args):
    try:
        if len(args) == 0:
            home_dir = str(pathlib.Path.home())
            os.chdir(home_dir)
        else:
            os.chdir(args)
    except Exception as e:
        print ("cd: no such file or directory: " + args)

def pause():
    

if __name__ == '__main__':
    main()
