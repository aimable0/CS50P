import random


def main():
    level = get_level()
    score = 0
    for _ in range(0, 10):
        x = generate_integer(level)
        y = generate_integer(level)
        trial = 0
        while True:
            try:
                answer = int(input(f"{x} + {y} = "))
            except ValueError:
                if trial != 2:
                    print("EEE")
                    trial += 1
                    pass
                else:
                    print("EEE")
                    print("{} + {} = {}".format(x, y, (x + y)))
                    break

            else:
                if answer == (x + y):
                    score += 1
                    break
                elif answer != (x + y) and trial != 2:
                    print("EEE")
                    trial += 1
                    pass
                else:
                    print("EEE")
                    print("{} + {} = {}".format(x, y, (x + y)))
                    break

    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in range(1, 4):
                return level
        except ValueError:
            pass


def generate_integer(level):
    ranges = {1: (0, 9), 2: (10, 99), 3: (100, 999)}
    return random.randint(*ranges[level])


if __name__ == "__main__":
    main()
