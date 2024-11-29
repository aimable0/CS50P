import sys
import requests

def main():
    bitcoins = get_coins()
    usd = convert(bitcoins)
    print(usd)


def convert(bitcoins):
    # get current bitcoin value
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    return "No price"


def get_coins():
    try:
        bitcoins = int(sys.argv[1])
        return bitcoins
    except ValueError:
        sys.exit("Command-line argument not a number")
    except IndexError:
        sys.exit("Missing command-line argument")


if __name__ == "__main__":
    main()
