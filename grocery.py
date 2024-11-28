from collections import Counter

def main():
    item_list = get_list()
    print_list(item_list)

def get_list():
    item_list = []
    while True:
        try:
            item = input()
        except EOFError:
            return sorted(item_list)
        else:
            item_list.append(item.upper())

def print_list(items_list):
    items = Counter(items_list)
    for item in items:
        print(f"{items[item]} {item}")

if __name__ == "__main__":
    main()