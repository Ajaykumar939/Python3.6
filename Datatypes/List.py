# A list is created by placing all the items (elements) inside square brackets [],
# separated by commas

ajay = [1, 2, 3]

my_list = []

x = [1, "Hello", 3.4]

y = ["mouse", [8, 4, 6], ['a']]

# Access List Elements
# We can use the index operator [] to access an item in a list.
# In Python, indices start at 0. So, a list having 5 elements will have an index from 0 to 4.

ajay = [1, 2, 3]
# print(ajay)

x = [1, "Hello", 3.4]
# print(x[1])

y = ["mouse", [8, 4, 6], ['a']]
# print(y[2])

# Negative indexing
# Python allows negative indexing for its sequences.
# The index of -1 refers to the last item, -2 to the second last item and so on.
ajay = [1, 2, 3]
# print(ajay[-1])
# print(ajay[2])

ajay = [1, 2, 3]
del ajay[1]
print(ajay)

# List Methods
# append() - Add an element to the end of the list
# extend() - Add all elements of a list to the another list
# insert() - Insert an item at the defined index
# remove() - Removes an item from the list

# ---append():
# syntax -
# list.append(item)
# The method takes a single argument
#
# item - an item to be added at the end of the list
# The item can be numbers, strings, dictionaries, another list, and so on.

x = ['pk', 'ntr']
# print("before append",x)
x.append("MB")
x.append("AJAY")
# print("after append", x)

# syntax - list1.extend(iterable)
x = ['pk', 'ntr']
print("before extend",x)
y = ['xyz', 'abc']
x.extend(y)
print("after extend", x)


ajay = [1, 2, 3, 1,2,3]
print(ajay)
