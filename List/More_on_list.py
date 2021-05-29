# Some functions in random module that can be used with lists

from random import choice, sample, shuffle

names = ["Naruto", "Kakashi", "Sasuke", "Sakura"]

name = choice(names)  # Picks up random item from list
print("Randomly selected name is ", name)

sample_name = sample(names, 2)  # picks a group of n random items from names
print(sample_name)

shuffle(names)  # The shuffle function modifies the original list
print(names)

# List Comprehension

# creating a list of first 10 positive number
list1 = [i for i in range(1, 11)]
print(list1)

# creating a list of square of first 10 positive numbers
list2 = [i**2 for i in range(1, 11)]
print(list2)

# creating a list of even numbers below 20
# [i for i in range(2,21,2)] is also an approach
list3 = [i for i in range(1, 21) if i % 2 == 0]
print(list3)

# creating a 2-D list
list4 = [[i, j] for i in range(3) for j in range(3)]
print(list4)
