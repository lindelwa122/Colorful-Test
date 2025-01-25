import subprocess
from sys import argv
import os


def main():
    args = argv[1:]

    if len(args) < 2:
        print('Usage: python -m colorful-test <directory_name>/<file_name>')


def execute_file(filename):
    subprocess.run(['python3', filename], capture_output=True, text=True)


def run_tests(args):
    for arg in args:
        if os.path.isdir(arg):
            run_tests(os.listdir(arg))

        elif arg.startswith('test') and arg.endswith('.py'):
            execute_file(arg)


if __name__ == '__main__': main()
