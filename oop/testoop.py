def main():
    name, house = get_student()
    print(type(name))
    


def get_student():
    name = input("Name: ")
    house = input("house: ")
    return (name, house)


if __name__ == "__main__":
    main()
