# playing aaround with tuples and * (unpack operator)

numbers = (10, 34, 12)
print(numbers)
print(*numbers)


def print_names(*args, **kwargs):
    # args that are not keyword / i.e argument not assigned to a named parameter
    # are collected into a tuple (*args)
    print(args)

    # args that are keyword arguments.. or that have named parameters assigned to them
    # ex name="kamanzi" are collected into a dictionary using (**kwargs)
    print(kwargs['name'])

names = 'Nkurikiyimana aimable'
print_names(names, "Aimable", "Karaake", "Ibirayi", "amazi", name='Kamanzi', age="18")



def print_sum(*args):
    print(sum(args))


print_sum(1, 4, 5, 6)

ages = (10, 34)
print(sum(ages))
