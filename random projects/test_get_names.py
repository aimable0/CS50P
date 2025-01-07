def get_names():
    user_names = []
    try:
        while True:
            name = input("Name: ")
            user_names.append(name)
    except EOFError:
        pass
    return user_names

def main():
    names = get_names()
    print(names)

main()
