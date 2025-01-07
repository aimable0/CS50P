import sys
import requests


def main():
    bitcoins = get_coins()
    usd = convert(bitcoins)
    print(f"{usd:,.4f}")


def convert(bitcoins):
    # geting current bitcoin value vi an api for the coinDesk Bitcoind Price Index
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    except requests.RequestException:
        sys.exit("Couldn't get required data")
    data = response.json()
    # current bitcoin rate_float
    rate_float = data["bpi"]["USD"]["rate_float"]
    return bitcoins * rate_float


def get_coins():
    try:
        bitcoins = float(sys.argv[1])
        return bitcoins
    except ValueError:
        sys.exit("Command-line argument not a number")
    except IndexError:
        sys.exit("Missing command-line argument")


if __name__ == "__main__":
    main()
