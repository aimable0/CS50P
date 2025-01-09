class Jar:

    def __init__(self, capacity):
        self.capacity = capacity
        self._size = 0

    def __str__(self):
        return f"🍪" * self._size

    def deposit(self, n):
        if self._size + n <= self._capacity:
            self._size += n
        else:
            raise ValueError("Can't add that much of cookies!")

    def withdraw(self, n):
        if self._size - n >= 0:
            self._size -= n
        else:
            raise ValueError("Not that much of cookies to withdraw!")

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity > 0:
            self._capacity = capacity
        else:
            raise ValueError("Invalid Number, non-negative can't be used of capacity")

    @property
    def size(self):
        return self._size


jar = Jar(10)
print(jar.capacity)
print(jar)