# Creating String

greet1 = 'Hello, World!'  # Single quote to create string
greet2 = "Hello, World!"  # Double quote to create string
greet3 = """ This string is created
using triple quotes"""

print("greet1 = ", greet1)
print("greet2 = ", greet2)
print("greet3 = ", greet3)

# input

userInput = input("Enter Something : ")
print("Type of userInput : ", type(userInput))

# Indexing

name = "ABCDEA"
print("name[0] = ", name[0])
print("name[2] = ", name[2])

# Slicing

print("Slice 1 = ", name[1:4])
print("Slice 2 = ", name[:4])
print("Slice 3 = ", name[1:])
print("Slice 4 = ", name[:])
print("Slice 5 = ", name[1:4:2])
print("Slice 6 = ", name[::2])
print("Slice 6 = ", name[::])
print("Changing value at index 3 = ", name[:3] + "m" + name[4:])

# Concatenation and repetition

str1 = "First "
str2 = "Second"
print("concatenation = ", str1 + str2)
print("Repetition = ", str1 * 3)

# searching in string
if "ABC" in name:
    print("abc in name")

if "G" not in name:
    print("g not in name")

# for loop in string

for i in range(len(name)):
    print(name[i], end="")
print()

for c in name:
    print(c, end="")
print()

# Methods in string
print("Convert to lower = ", name.lower())
print("Convert to upper = ", name.upper())
print("Replace every occurance of A = ", name.replace("A", "Z"))
print("index of a = ", name.index("A"))
# print("index of m in name = ", name.index("m")) This will throw error since m is not in name
print("Is Every character of name is a letter = ", name.isalpha())
