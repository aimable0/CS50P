with open("names.csv") as file:
    for line in file:
        # Let's approach this by unpacking the items in the list and saving them to respective vars
        (col1, col2) = line.rstrip().split(',')
        print(f"Name: {col1}, and age: {col2}")
