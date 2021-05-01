# for <variable> in <sequence>:
#    # body_of_loop that has set of statements
#    # which requires repeated execution

# range(n): generates a set of whole numbers starting from 0 to (n-1).
# for i in range(10):
#     print(i)

# range(start, stop): generates a set of whole numbers starting from start to stop-1.
# for i in range(0,111):
#     print(i)

# range(start, stop, step_size): The default step_size is 1 which is why when we didn’t specify the step_size, the numbers generated are having difference of 1. However by specifying step_size we can generate numbers having the difference of step_size.
for i in range(1,100,2):
    print(i)

x = [1,2,4,5,6,7,8,9]
print(x)

for i in x:
    print(i)

for i in "AJAY":
    print(i)

for val in range(5):
	print(val)
else:
	print("The loop has completed execution")