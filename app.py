import subprocess

def greet(name):
	print(f"Hello, {name}!")

def run_command(cmd):
	subprocess.call(cmd, shell=True)

if __name__ == "__main__":
	name = input("Enter your name: ")
	greet(name)

	cmd = input("Enter a command to run: ")
	run_command(cmd)
