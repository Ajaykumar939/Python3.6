# class parent_class:
# body of parent class
#
# class child_class( parent_class):
# body of child class



# There are five types of inheritances:
#
# Single Inheritance
# Multiple Inheritance
# # Multilevel Inheritance
# # Hierarchical Inheritance
# # Hybrid Inheritance

# single inheritance:

# class parent:
#    statement1
#    statement2
#    .
#    .
# class child(parent):
#    statement1
#    statement2

#Multiple inheritance:

# class grandfather:
#    statement1
#    statement2
#    .
#    .
# class father:
#    statement1
#    statement2

# class child(grandfather, father):
# # #  statement1
# # #    statement2
#
# #multilevel inheritance
#
# # class father:
# #    statement1
# #    statement2
# #    .
# #    .
# # class ajay(father):
# #    statement1
# #    statement2
#
# # class vijay(ajay):
# # #  statement1
# # #    statement2
#
# #hierarchy
#
# # class parent:
# #    statement1
# #    statement2
#
# # class child1(parent):
# #    statement1
# #    statement2
#
# # class child2(parent):
# # #  statement1
# # #    statement2
#
# # class child3(parent):
# # #  statement1
# # #    statement2
#
#
# # Python program to demonstrate
# # single inheritance
#
#
# # Base class
# # class Parent:
# # 	def func1(self):
# # 		print("This function is in parent class.")
# #
# # 	def func2(self):
# # 		print("This function2")
# #
# # # Derived class
# # class Child(Parent):
# # 	def func3(self):
# # 		print("This function is in child class.")
# #
# # 	def func4(self):
# # 		print("This function4")
# #
# #
# #
# # # Driver's code
# # object = Child()
# # object.func1()
#
# # Python program to demonstrate
# # multiple inheritance
#
#
# # Base class1
# # class GrandMother:
# # 	def grandmother(self):
# # 		print("GrandMother")
# #
# # # Base class2
# # class Father:
# # 	def father(self):
# # 		print("Father")
# #
# # # Derived class
# # class Son(GrandMother, Father):
# # 	def son(self):
# # 		print("SON")
# #
# # # Driver's code
# # s1 = Son()
# # s1.father()
# # s1.grandmother()
#
# # Python program to demonstrate
# # multilevel inheritance
#
# # Base class
# # class Grandfather:
# #     def grandfather(self):
# #         print("Grandfather")
# #
# # # Derived class
# # class Father(Grandfather):
# #     def father(self):
# #         print("father")
# #
# # # Derived class
# # class Son(Father):
# #     def son(self):
# #         print("son")
# # # Driver code
# # s1 = Son()
# # s1.son()
# # s1.grandfather()
# # s1.father()
#
# # Python program to demonstrate
# # Hierarchical inheritance
#
#
# # Base class
# class Parent:
# 	def func1(self):
# 		print("This function is in parent class.")
#
# # Derived class1
# class Child1(Parent):
# 	def func2(self):
# 		print("This function is in child 1.")
#
# # Derivied class2
# class Child2(Parent):
# 	def func3(self):
# 		print("This function is in child 2.")
#
# # Driver's code
object1 = Child1()
object2 = Child2()
object1.func1()
object1.func2()
object2.func1()
object2.func3()
