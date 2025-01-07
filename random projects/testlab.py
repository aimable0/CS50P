import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    try:
        match = re.search(r"(\d+):?(\d+)? ([A-Z]{2}) to (\d+):?(\d+)? ([A-Z]{2})", s)
        if match.group(3) == "AM":
            h1 = match.group(1) if match.group(1) != "12" else "00"
            h2 = str(int(match.group(4)) + 12) if match.group(4) != "12" else "12"
        else:
            h2 = match.group(4) if match.group(4) != "12" else "00"
            h1 = str(int(match.group(1)) + 12) if match.group(1) != "12" else "12"
            print(h2, h1)
        min1 = match.group(2) if match.group(2) != None else "00"
        min2 = match.group(5) if match.group(5) != None else "00"
        if int(h1) <= 12 and int(h2) <= 24 and int(min1) <= 59 and int(min2) <= 59:
            return f"{h1:02}:{min1} to {h2}:{min2}"
        elif int(h1) <= 24 and int(h2) <= 12 and int(min1) <= 59 and int(min2) <= 59:
            return f"{h1:02}:{min1} to {int(h2):02}:{min2}"
        else:
            raise ValueError
    except (AttributeError, ValueError):
        sys.exit("Invalid format")


if __name__ == "__main__":
    main()
