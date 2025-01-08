# create a class that ranks student.


class Rank:

    students = {"Aimable": 80, "JeanLuc": 90, "Uwase": 33, "Didier": 67, "Carine": 89}

    @classmethod
    def rank(cls):
        max_perc = None
        name = None
        for student, perc in cls.students.items():
            if max_perc == None:
                max_perc = perc
                name = student
            else:
                if perc < max_perc:
                    max_perc = perc
                    name = student

        return f"The most out-last_standing student is {name} with {max_perc}%"


print(Rank.rank())
