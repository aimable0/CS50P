from datetime import date
import inflect
import sys


def main():
    birth_day_date = get_birth_date()
    minutes_in_words = get_minutes(birth_day_date)
    print(minutes_in_words)


def get_birth_date():
    birth_date = input("Date of Birth: ")
    try:
        b_date = date.fromisoformat(birth_date)
    except ValueError:
        sys.exit()
    else:
        return b_date


def get_minutes(birth_day_date):
    # use the birth date and the current date to calculate days and min
    # we use '.days' to get the days attribute from the date object returned
    days = (date.today() - birth_day_date).days
    # we use days * min per day to get total minutes
    minutes = days * 1440

    # format min to words
    p = inflect.engine()
    word = p.number_to_words(minutes)
    return str(word).capitalize() + " minutes"


if __name__ == "__main__":
    main()
