from sys import argv
from typing import List
import subprocess
import os


def main() -> None:
    """
    This is the main function of the program. It runs tests inside a
    specified directory or executes the test file itself if provided.

    Usage: python -m colorful-test <directory_name>/<file_name>
    """

    args = argv[1:]

    if len(args) < 2:
        print('Usage: python -m colorful-test <directory_name>/<file_name>')


def execute_file(filename: str) -> None:
    """Uses subprocess to run a test file"""
    subprocess.run(['python3', filename], capture_output=True, text=True)


def run_tests(args: List[str]) -> None:
    """
    Takes a list of tests and runs them.
    """

    for arg in args:
        if os.path.isdir(arg):
            run_tests(os.listdir(arg))

        elif arg.startswith('test') and arg.endswith('.py'):
            execute_file(arg)


if __name__ == '__main__':
    main()
