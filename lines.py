import sys


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
        with open(file) as f:
            count = 0
            for line in f:
                if not line.startswith("# ") and line != "\n":
                    count += 1
    except FileNotFoundError:
        sys.exit("File does not exist")
    return count


if __name__ == "__main__":
    main()
