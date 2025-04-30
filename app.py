import subprocess
import shlex

def greet(name):
	print(f"Hello, {name}!")

def run_command(cmd):
	safe_cmd=shlex.split(cmd)
	subprocess.call(safe_cmd)

if __name__ == "__main__":
	name = input("Enter your name: ")
	greet(name)

	cmd = input("Enter a command to run: ")
	run_command(cmd)
