myset = {"apple", "banana", "cherry"}
newSet = {"pineapple", "mango", "papaya"}
newList = ["apple", "Guava", "Grapes"]

myset.add("strawberry")
print("myset after adding strawberry : ", myset)

# Update can take any iterable object like String,List,Tuple,Dictionary
myset.update(newSet)
print("After updating myset with newSet : ", myset)
myset.update(newList)
print("After updating myset with newList : ", myset)

myset.remove("banana")  # Throws error if the element is not present
print("After removing banana from myset : ", myset)


myset.discard("apple")  # does not throw error if element is not present
print("After discarding apple from myset", myset)

unionSet = myset.union(newSet) # Union of two sets
print("UnionSet : ", unionSet)

myset.intersection_update(unionSet) # Intersecting and updating at the same time
print("Intersectiong and updating together : ", myset)

intersectionSet = myset.intersection(unionSet) # Intersection returns a different set
print("Intersection Set : ", intersectionSet)

myset.clear()
print("After clearing mySet : ", myset)

