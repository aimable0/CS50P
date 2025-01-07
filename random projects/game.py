import random


def main():
    level = get_level()
    Number_to_match = random.randrange(1, level)
    guess_game(Number_to_match)


def get_level():
    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            pass
        else:
            if level <= 0:
                pass
            else:
                return level


def guess_game(number):
    while True:
        try:
            guess = int(input("Guess: "))
        except ValueError:
            pass
        else:
            if guess > number:
                print("Too large!")
                pass
            elif guess < number:
                print("Too small")
                pass
            else:
                print("Just right!")
                break

if __name__ == "__main__":
    main()
