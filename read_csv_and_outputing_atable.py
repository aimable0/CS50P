
print('Name     | age ')
print('---------|------')
with open("names.csv") as file:
    for line in sorted(file):
        # Let's approach this by "unpacking" the items in the list in sequence and saving them to respective vars
        col1, col2 = line.rstrip().split(',')
        if len(col1) < 9:
            col1 = col1 + (" " * (9 - len(col1)))
        print(f"{col1}| {col2}")