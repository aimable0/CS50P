def main():
    fraction = get_fraction()
    print_percentage(fraction)


def get_fraction():
    while True:
        fraction = (input('Fraction: ')).strip()
        try:
            x = int(fraction.split('/')[0])
            y = int(fraction.split('/')[1])
        except (ValueError, ZeroDivisionError):
            pass
        else:
            if x <= y and y != 0:
                return x / y
            pass

def print_percentage(fraction):
    percentage = round(fraction * 100)
    if percentage == 100:
        print('F')
    elif percentage <= 1:
        print('E')
    else:
        print(f"{percentage}%")

main()

