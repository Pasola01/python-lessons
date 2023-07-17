class Person:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def person_description(self):
        print("my name is " + self.name + " am " + str(self.age))



var = Person("alex", 31, 62)
var.person_description()