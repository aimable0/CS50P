names = ['Aimable', 'Aimable', 'Carine', 'Didier']
print('Adieu, adieu to ', end="")

for name in names:
    if name == names[-1]:
        print(('and ' if len(names) > 1 else '') + name) # Last name or only name.
    else:
        print(name, end=', ' if len(names) > 2 else ' ')