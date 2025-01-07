import re


def main():
    print(count(input("Text: ")))


def count(s):
    occurence = re.findall(r"^um| um[^a-z]", s.lower(), )
    return len(occurence)


if __name__ == "__main__":
    main()
