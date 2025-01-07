def main():
    """
    Main function to validate an IPv4 address provided by the user.
    """
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    """
    Validate an IPv4 address.

    Args:
        ip (str): The IPv4 as a string.

    Returns:
        bool: True if the input is valid IPv4 address, False otherwise.
    """
    try:
        # Split the input string to separate potential IP segments.
        # Filter and keep only numbers in the valid IPv4 range(0-255).
        address_nums = [num for num in ip.split(".") if int(num) in range(0, 256)]
        # check if the address contains exactly four segments to be valid.
        return True if len(address_nums) == 4 else False
    except ValueError:
        # returns False if any non-integer is detected.
        return False


if __name__ == "__main__":
    main()
