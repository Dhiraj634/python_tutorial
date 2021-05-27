# printing hello 10 times
for i in range(10):
    print("Hello")

# loop variable

for i in range(10):
    print(i)

for loopCount in range(10):
    print(loopCount)

for i in range(10):
    # print(i, end=" ")
    print(i, end="*")

# range function

for i in range(10):
    print(i, end=" ")

for i in range(4, 10):
    print(i, end=" ")

for i in range(1, 10, 2):
    print(i, end=" ")

# printing pattern
for i in range(5):
    print("*" * 6)

# nesting for loops

for i in range(5):
    for j in range(5):
        print(i, end=" ")
    print()
