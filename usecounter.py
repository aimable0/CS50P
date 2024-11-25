from collections import Counter

groceries_list = ['vegetables', 'onion', 'rosemarry', 'lettuces', 'tomato', 'onion', 'tomato', 'lettuces', 'onion', 'rosemarry']

counter = Counter(groceries_list)
print(counter)

for item in counter:
    print(f"{counter[item]} {item.upper()}")

# name = 'Aiamableea'
# counter_1 = Counter(name)
# print(counter_1)