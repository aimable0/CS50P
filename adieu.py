def main():
    names = get_names()
    print_names(names)


def get_names():
    user_names = []
    while True:
        try:
            name = input("Name: ")
        except EOFError:
            print()
            return user_names
        else:
            user_names.append(name)

def print_names(names):
    print("Adieu, adieu to ", end="")

    for name in names:
        if name == names[-1]:
            print(("and " if len(names) > 1 else "") + name)  # Last name or only name.
        else:
            print(name, end=", " if len(names) > 2 else " ")


if __name__ == "__main__":
    main()
