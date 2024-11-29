import random


def main():
    level = get_level()
    score = 0
    for _ in range(0, 10):
        x = generate_integer(level)
        y = generate_integer(level)
        correct_answer = x + y
        trial = 0
        while True:
            try:
                answer = int(input(f"{x} + {y} = "))
            except ValueError:
                if trial != 2:
                    trial = wrong_answer(trial)
                    pass
                else:
                    output_answer(x, y)
                    break
            else:
                if answer == correct_answer:
                    score += 1
                    break
                elif answer != correct_answer and trial != 2:
                    trial = wrong_answer(trial)
                    pass
                else:
                    output_answer(x, y)
                    break
    print(f"Score: {score} / 10")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            pass
        else:
            if level not in range(1, 4):
                pass
            else:
                return level


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    if level == 2:
        return random.randint(10, 99)
    if level == 3:
        return random.randint(100, 999)


def wrong_answer(trial):
    print("EEE")
    trial += 1
    return trial

def output_answer(x, y):
    print("EEE")
    print("{} + {} = {}".format(x, y, (x + y)))


if __name__ == "__main__":
    main()
