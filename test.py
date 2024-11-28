names = ['Aimable']
names.insert(0, 'Adieu, adieu')
names[1] = 'to ' + names[1]
greeting = 'Adieu, adieu'

if len(names) == 2:
    for name in names:
        if name == names[-1]:
            print(name)
        else:
            print(name, end=', ')

else:
    for name in names:
        if name == names[-1]:
            print('and', name)
        else:
            print(f"{name}", end=', ' if len(names) > 2 else ' ')
