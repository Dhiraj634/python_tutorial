marks = [8, 7, 5, 6, 6, 9, 7, 8]
length = len(marks)  # get the length of the list
print()
print("*" * 70)
print()
# "in" keyword can be used to search in the list

print("marks = ", marks)
if 9 in marks:
    print("9 is present in the list")
if 4 not in marks:
    print("4 is not in marks list")

# indexing
# using index to access the element of list
# list indexing always starts with 0 i.e. first element is at index 0
print("marks[0] = ", marks[0])
print("marks[1] = ", marks[1])

# Slicing

print("slice 1 = ", marks[1:5])
print("slice 2 = ", marks[:5])
print("slice 3 = ", marks[1:])
print("slice 4 = ", marks[::1])


# + and * operators
print("+ Operator = ", [1, 2] + [3, 4, 5])
print("* Operator = ", [1, 2] * 3)
print("Creating array of zeros = ", [0] * 5)

# looping in list
print("First Loop : ", end="")
for i in range(len(marks)):
    print(marks[i], end=" ")

print()

print("Second Loop : ", end="")
for mark in marks:
    print(mark, end=" ")

print()

# Built-in functions

length = len(marks)
print("Length of marks = ", length)
total = sum(marks)
print("Sum of marks = ", total)
minimum = min(marks)
print("minimum of marks = ", minimum)
maximum = max(marks)
print("maximum of marks = ", maximum)
# average = sum(marks)/len(marks)

# List methods

print("marks = ", marks)

marks.append(10)
print("After append = ", marks)

marks.sort()
print("after sort = ", marks)

print("count of 6 ", marks.count(6))

print("first occurance of 6 ", marks.index(6))

marks.reverse()
print("after reverse = ", marks)

marks.remove(6)
print("after remove = ", marks)

marks.pop(2)
print("after pop = ", marks)

marks.insert(2, 12)
print("after insert = ", marks)

# copy list
copied_marks = marks[:]
print(f" marks id = {id(marks)}")
print(f"copied_marks id = {id(copied_marks)}")
