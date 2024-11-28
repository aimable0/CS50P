# programm that format the date to YYYY-MM-DD


def main():
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]
    while True:
        input_date = input("Date: ").strip()
        if " " in input_date:
            date = input_date.split(" ")
            if date[0] in months and int(date[1].replace(",", "")) <= 31:
                print(
                    f"{int(date[2])}-{(months.index(date[0]) + 1):02}-{int(date[1].replace(',', "")):02}"
                )
                break
            else:
                pass

        date = input_date.split("/")
        if int(date[0]) in range(1, 12):
            print(f"{int(date[2])}-{int(date[0]):02}-{int(date[1]):02}")
            break
        pass

if __name__ == "__main__":
    main()
