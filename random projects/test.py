import sys
import re


def main():
    if len(sys.argv) == 2:
        try:
            if sys.argv[1].split(".")[1] == "py":
                lines = count_lines(sys.argv[1])
                print(lines)
            else:
                sys.exit("Not a python file")
        except IndexError:
            sys.exit("Not a python file")
    else:
        (
            sys.exit("Too many command-line arguments")
            if len(sys.argv) > 2
            else sys.exit("Too few command-line arguments")
        )


def count_lines(file):
    """
    function that counts lines of code in provided python file.

    Args:
        file (python file): file that contains lines of code

    Returns:
        int: total number of lines of code
    """
    try:
        count = 0
        with open(file) as f:
            for line in f:
              if not line.isspace() and not line.startswith("#"):
                  count += 1
        return count
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()
