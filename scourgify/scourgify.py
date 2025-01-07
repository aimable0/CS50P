import sys
import csv


def main():
    if len(sys.argv) == 3:
        try:
            if (
                sys.argv[1].split(".")[1] == "csv"
                and sys.argv[2].split(".")[1] == "csv"
            ):
                old_file = sys.argv[1]
                new_file = sys.argv[2]
                write_csv(old_file, new_file)
        except FileNotFoundError:
            sys.exit("Could not read invalid_file.csv")
    else:
        (
            sys.exit("Too few command-line arguments")
            if len(sys.argv) < 3
            else sys.exit("Too many command-line arguments")
        )


def write_csv(old_file, new_file):
    with open(old_file) as file:
        reader = csv.reader(file)
        data = []
        for names, house in reader:
            if ", " in names:
                names = names.split(" ")
                data.append([names[1], names[0][:-1], house])
            else:
                data.append([names, house])

    with open(new_file, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["first", "last", "house"])
        writer.writerows(data[1:])


if __name__ == "__main__":
    main()
