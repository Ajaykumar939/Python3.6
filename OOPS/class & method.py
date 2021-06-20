# class----girls, boys
# girls---behaviour
# boys---behaviour
#
# class ECE:
#     '''demo for class'''
#     def Ajay(self):
#         print('I am ajay...')
#     def Sai(self):
#         print('I am sai...')
# result = ECE()
# result.Ajay()
# result.Sai()
# result.Ramu()


# man
# objects = attributes(height, weight, color) + behaviour(walking, talking, eating, slepping)

# shop
# objects = attributes(name, year) + behaviour(selling, buying)

class Human():
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight
    def eating(self, food):
        """Object
        attributes: name, height, weight
        Object
        behaviour: eating()"""
        return "{} is eating {}".format(self.name, food)
# creating objects of class Human
ram = Human("Ram", 6, 60)
steve = Human("Steve", 5.9, 56)

print("Height of {} is {}".format(ram.name, ram.height))
print("Weight of {} is {}".format(ram.name, ram.weight))
print(ram.eating("Pizza"))
print("Weight of {} is {}".format(steve.name, steve.height))
print("Weight of {} is {}".format(steve.name, steve.weight))
print(steve.eating("Big Kahuna Burger"))

