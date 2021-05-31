mytuple = ("apple", "banana", "cherry", "mango")

# While creating singel element tuple keep in mind to provide "," else it will treat it as string
singleElemetTuple = ("apple",)

print("My tuple : ", mytuple)
print("Type : ", type(mytuple))

# indexing
print("Index 0 : ", mytuple[0])
print("Index 1 : ", mytuple[1])
print("Index 2 : ", mytuple[2])

# Slicing

print("Slice1 : ", mytuple[1:3])
print("Slice2 : ", mytuple[1:])
print("Slice3 : ", mytuple[:3])
print("Slice4 : ", mytuple[::2])
print("Slice5 : ", mytuple[:])
print("Slice6 : ", mytuple[::])

# Concatenation and Repetition

print("Concatenation : ", ("abc", "def") + ("ghi", "jkl"))
print("Repetition : ", ("abc", "def") * 3)

# Searching in tuple
mytuple = ("apple", "banana", "cherry", "mango")
isPresent = "mango" in mytuple
print("Searching mango in mytuple : ", isPresent)

# Looping over tuple
print("Index wise looping : ", end=" ")
for i in range(len(mytuple)):
    print(mytuple[i], end=" ")

print()

print("Element wise looping : ", end=" ")
for element in mytuple:
    print(element, end=" ")

print()

# Unpacking in tuple [it also works same in list as well]
names = ("Naruto", "Kakashi", "Sakura", "Sasuke")
(name1, name2, name3, name4) = names
print(name1, name2, name3, name4)
(master, *team) = names
print(master, team)
(first, *second, third) = names
print(first, second, third)
