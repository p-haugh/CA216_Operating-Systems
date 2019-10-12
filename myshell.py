#!/usr/bin/env python3
import cmd, os, sys, threading, multiprocessing, shell_commands

def main():

    prompt = shell_commands.shell()
    intro = "Welcome! Type  ? to list commands"

    # No batchfile contained in command prompt
    if len(sys.argv) == 1:
        prompt.prompt = os.environ["PWD"] + "/> "
        prompt.cmdloop(intro)
    # Batchfile contained in command prompt
    else:
        with open (sys.argv[1], "r") as batchfile:
            argv_file = batchfile.readlines()

            



if __name__ == '__main__':
    main()
