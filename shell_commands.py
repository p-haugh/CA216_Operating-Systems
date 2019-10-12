import cmd, os, sys, threading, multiprocessing, subprocess
lock = threading.Lock()

class shell(cmd.Cmd):


	prompt = "myshell> "
	shell = os.getcwd() + "/myshell"
	help = ""

	def default(self, args):
		"Allow external commands to be run in the shell."
		try:
			subprocess.call(args.split())
		except FileNotFoundError:
			print ("This file does not exist.")
		except PermissionError:
			print ("You do not have access to this file.")

	def do_cd(self, args):
		"change the current default directory to <directory>.\nUsage: cd <directory>\n"
		if args == "":
			print (os.getcwd())
		else:
			if os.args.isdir(args):
				os.chdir(args)
				shell.prompt = os.getcwd() + "/> "
				os.environ["PWD"] = os.getcwd()
			else:
				print(args + " is not a directory")

	def do_clr(self, args):
		"Clear the contents of the shell.\nUsage: clr.\n"
		print("\033[2J\033[H", end="")

	def do_dir(self, args):
		"List the contents of directory <directory>.\nUsage: cd <directory>\n"
		if args == "":
			print (os.listdir())
		else:
			if os.path.isdir(args):
				print (os.listdir(args))
			else:
				print(args + " is not a directory")

	def do_environ(self, args):
		"List all the environment strings.\nUsage: environ\n"
		results = ""
		for s in os.environ:
			results += "KEY: "+ s + " File: " + os.environ[s] + "\n"
		print (results.rstrip())

	# Echo shell
	def do_echo(self, args):
		"Display <comment> on the display followed by a new args.\nUsage: echo <comment>.\n"
		clean_string = ' '.join(args.split())
		print (clean_string + "\n")

	# help with more filter

	def do_pause(self, args): # Command to pause the shell until 'Enter' is pressed.
		"Pause operation of the shell until 'Enter' is pressed."
		input("Paused, press Enter to continue...")
		print ()

		lock.aquire()
		i = input()

	# Quit the shell
	def do_quit(self, args):
		"Quit the shell."
		print("Quitting the shell, Goodbye!")
		return True

	def emptyline(self): # Do nothing if no command is entered.
		pass

if __name__ == '__main__':
	shell().cmdloop()
