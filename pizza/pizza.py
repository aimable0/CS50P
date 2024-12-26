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
        i = 0
        for col1, col2, col3 in reader:
            if i == 0:
                print("+------------------+---------+---------+")
                print(
                    "|{}|{}|{}|".format(
                        (" " + col1 + ((17 - len(col1)) * " ")),
                        (" " + col2 + ((8 - len(col2)) * " ")),
                        (" " + col3 + ((8 - len(col3)) * " ")),
                    )
                )
                print("+==================+=========+=========+")
            else:
                print(
                    "|{}|{}|{}|".format(
                        (" " + col1 + ((17 - len(col1)) * " ")),
                        (" " + col2 + ((8 - len(col2)) * " ")),
                        (" " + col3 + ((8 - len(col3)) * " ")),
                    )
                )
                print("+------------------+---------+---------+")
            i += 1


if __name__ == "__main__":
    main()
