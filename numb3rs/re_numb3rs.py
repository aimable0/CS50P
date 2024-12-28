import re


def main():
    print(validate(input("IPv4 Address: ").strip()))


def validate(ip):
    if matches := re.search(r"([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+)", ip):
        valid_num = [num for num in matches.groups() if int(num) <= 255]
        return True if len(valid_num) == 4 else False
    return False


if __name__ == "__main__":
    main()
