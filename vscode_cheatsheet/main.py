import os

from pandas import DataFrame

from vscode_cheatsheet.utils import my_util
from vscode_cheatsheet.utils import my_util


def main() -> None:
    """Function that writes Hello World! to the console and the current PYTHONPATH"""
    print("Hello World!")
    print(f"PYTHONPATH={os.environ.get('PYTHONPATH')}")
    my_util()


if __name__ == "__main__":
    main()
