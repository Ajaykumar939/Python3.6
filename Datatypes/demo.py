# Variables can store data of different types, and different types can do different things.
#
# Python has the following data types built-in by default, in these categories:
#
# Text Type:	str- 'letters, 'words, 'char'
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview

x = 5
print(type(x))

x = "Hello World"
print(type(x))

x = 20.0
print(type(x))

x = ["apple", "banana", "cherry"]
print(type(x))

x = ("apple", "banana", "cherry")
print(type(x))

x = {"name" : "John", "age" : 36}
print(type(x))

x = {"apple", "banana", "cherry"}
print(type(x))

x = True
print(type(x))

x = b"Hello"
print(type(x))