class Person:
    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

    def description_person(self):
        description = "My name is " + self.name + " Im " + str(self.age) + " " + "my height is " + str(self.weight) + " " + "and weight " + str(self.height)
        print(description)

    def man_weight(self):
        print("My real weight is: " + str(self.weight))

    def man_weight_update(self, kg):
        self.weight = kg



class Warrior(Person):
    def __init__(self, name, age, weight, height):
        super().__init__(name, age, weight, height)
        self.rage = 100

    def warrior_rage(self):
        print("My rage is: " + str(self.rage))

    def description_warrior(self):
        description = "My name is " + self.name + " Im " + str(self.age) + " my rage " + str(self.rage)
        # print(description)
        return description




warrior_1 = Warrior("Conan", 40, 195, 120)
# warrior_1.man_weight_update(150)
# warrior_1.description_person()
# warrior_1.description_warrior()



# man_1 = Person("Yurii", 31, 62, 165)
# man_1.description_person()


