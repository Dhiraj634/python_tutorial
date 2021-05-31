# Unpacking in tuple
names = ("Naruto", "Kakashi", "Sakura", "Sasuke")
(name1, name2, name3, name4) = names
print(name1, name2, name3, name4)
(master, *team) = names
print(master, team)
(first, *second, third) = names
print(first, second, third)