class Building:
    def __init__(self, numFloor, containsLift):
        self.numFloor = numFloor
        self.containsLift = containsLift


twoFloorBuilding = Building(4, True)
threeFloorBuilding = Building(3, False)


class Dog:
    species = "Dog"

    def __init__(self, breed, color):
        self.breed = breed
        self.color = color

    def getBreed(self):
        return self.breed

    def getColor(self):
        return self.color


husky = Dog("Husky", "Black")
bullDog = Dog("BullDog", "Creamy")
print("Husky Color", husky.getColor())
print("Bulldog Breed", bullDog.getBreed())
