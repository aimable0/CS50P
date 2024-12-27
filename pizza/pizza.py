from tabulate import tabulate
import sys
import csv


def main():
    if len(sys.argv) == 2:
        try:
            if sys.argv[1].split(".")[1] == "csv":
                print_table(sys.argv[1])
            else:
                sys.exit("Not a CSV file")
        except IndexError:
            sys.exit("Not a CSV file")
    else:
        (
            sys.exit("Too few command-line arguments")
            if len(sys.argv) < 2
            else sys.exit("Too many command-line arguments")
        )


def print_table(filename):
    with open(filename) as file:
        reader = csv.reader(file)
        data = [line for line in reader]
        content = data[1:]
        print(tabulate(content, headers=data[0], tablefmt="grid"))


if __name__ == "__main__":
    main()
