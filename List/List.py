marks = [8, 7, 5, 6, 6, 9, 7, 8]
length = len(marks)  # get the length of the list

# "in" keyword can be used to search in the list

if 9 in marks:
    print("9 is present in the list")
if 4 not in marks:
    print("4 is not in marks list")

# indexing
# using index to access the element of list
# list indexing always starts with 0 i.e. first element is at index 0
print(marks[0])
print(marks[1])

# count method in list
count_of_six = marks.count(6)
print(count_of_six)

# + and * operators
print([1, 2] + [3, 4, 5])
print([1, 2] * 3)
print([0] * 5)

# looping in list
for i in range(len(marks)):
    print(marks[i], end=" ")

print()

for mark in marks:
    print(mark, end=" ")

print()

# Built-in functions

length = len(marks)
total = sum(marks)
minimum = min(marks)
maximum = max(marks)
# average = sum(marks)/len(marks)

# List methods

marks.append(10)
print(marks)

marks.sort()
print(marks)

print("count of 6 ", marks.count(6))

print("first occurance of 6 ", marks.index(6))

marks.reverse()
print(marks)

marks.remove(6)
print(marks)

marks.pop(2)
print(marks)

marks.insert(2, 12)
print(marks)

# copy list
copied_marks = marks[:]
print(f" marks id = {id(marks)}")
print(f"copied_marks id = {id(copied_marks)}")
