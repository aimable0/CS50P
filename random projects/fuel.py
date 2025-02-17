def main():
    fraction = convert()
    gauge(fraction)


def convert():
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

def gauge(fraction):
    percentage = round(fraction * 100)
    if percentage >= 99:
        print('F')
    elif percentage <= 1:
        print('E')
    else:
        print(f"{percentage}%")

if __name__ == "__main__":
    main()

