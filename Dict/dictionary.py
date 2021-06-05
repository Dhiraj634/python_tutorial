d = {'A': 100, 'B': 200}

print("Value of A ", d['A'])
d['C'] = 300
print("After inserting C : ", d)

del d['A']
print("After deleting A : ", d)

isPresent = "A" in d  # false because we have deleted A above
print("Is A present : ", isPresent)

print("Keys : ", end="")
for key in d:
    print(key, end=" ")
print()

print("Values : ", end="")
for value in d.values():
    print(value, end=" ")
print()

print("Key : Value pairs = ", end="")
for pair in d.items():
    print(f"{pair[0]}:{pair[1]}", end=" ")
print()

d1 = d.copy()
d1["C"] = 1000
print("d1 = ", d1)
print("d = ", d)

words = ["Dog", "Elephant"]

animalDict = {word: len(word) for word in words}
print("AnimalDict = ", animalDict)
