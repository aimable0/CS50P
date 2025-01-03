import re


def main():
    print(validate(input("IPv4 Address: ").strip()))


def validate(ip):
    try:
        matches = re.search(r"([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+)", ip)
        valid_num = [num for num in matches.groups() if int(num) <= 255]
    except AttributeError:
        return False
    else:
        return True if len(valid_num) == 4 else False


if __name__ == "__main__":
    main()


