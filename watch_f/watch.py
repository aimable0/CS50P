import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if matches := re.search(
        r'src="https?://(?:www\.)?youtube.com/embed/(\w+)".+</iframe>$', s
    ):
        return "https://youtu.be/" + matches.group(1)
    return None


if __name__ == "__main__":
    main()
