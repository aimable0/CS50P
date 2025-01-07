from validator_collection import checkers


def main():
    print(validate_email(input("What's your email?  ").strip()))


def validate_email(s):
    return "Valid" if checkers.is_email(s) else "Invalid"


if __name__ == "__main__":
    main()
