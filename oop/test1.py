class Hat:
    def sort(self, name):
        print(name, 'is in', "some hosue")

hat = Hat()
hat.sort("harry")
Hat.sort(hat, "Harry")