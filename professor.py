import random


def main():
    level = get_level()
    score = 0

    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        if ask_question(x, y):
            score += 1

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


def ask_question(x, y):
    correct_answer = x + y
    for trial in range(3):
        try:
            answer = int(input(f"{x} + {y} = "))
            if answer == correct_answer:
                return True
        except ValueError:
            pass
        print("EEE")

    print(f"{x} + {y} = {correct_answer}")
    return False


if __name__ == "__main__":
    main()
