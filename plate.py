import re

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

# maj-check function
def is_valid(s):
    s = s.strip()
    # complete check
    return (
        starts_with_2_letters(s)
        and valid_length(s)
        and only_num_and_al(s)
        and no_num_in_the_middle(s)
    )

#check functions
def starts_with_2_letters(x):
    return len(x) >= 2 and x[0].isalpha() and x[1].isalpha()

def valid_length(x):
    return (2 <= len(x) <=6)

def only_num_and_al(x):
    return x.isalnum()

def no_num_in_the_middle(plate):
    if plate.isalpha():
        return True
    # find the first digit in plate
    first_num = re.findall(r"\d", plate)[0]
    if first_num == '0':
        return False
    # check if the substring from the first number to the end is numeric
    return plate[plate.index(first_num):].isnumeric()

if __name__ == "__main__":
    main()

