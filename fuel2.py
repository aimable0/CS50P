def main():
    percentage_number = convert(input('Fraction: ').strip())
    percentage = gauge(percentage_number)
    print(percentage)

def convert(input_text):
    try:
        x = int(input_text.split('/')[0])
        y = int(input_text.split('/')[1])
        if y == 0:
            raise ZeroDivisionError
        elif x > y:
            raise ValueError
        else:
            return round((x / y) * 100)
    except IndexError:
        raise ValueError

def gauge(p_num):
    return 'F' if p_num >= 99 else 'E' if p_num <= 1 else f"{p_num}%"

if __name__ == "__main__":
    main()