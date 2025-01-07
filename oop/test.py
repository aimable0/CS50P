class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if name != None:
            self._name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if age > 0:
            self._age = age

    def __str__(self):
        return f"{self.name} is {self.age}"


student = Student("Aimable", 0)
student.age = 0
print(student)
