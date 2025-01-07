from emoji import emojize


def main():
    text = input("Input")
    emojized_output = emojize(text, language="alias")
    print(f"Output: {emojized_output}")


if __name__ == "__main__":
    main()
