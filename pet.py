class Pet:
    def __init__(self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 100
        self.energy = 100

    def sleep():
        self.energy += 25
        return self
    def eat():
        self.energy += 5
        self.health += 10
        return slef
    def play():
        self.health += 5
        return self
    def noise():
        print("aaa!")
        return self


class Ninja:
    def __init__(self, first_name, last_name, treats, pet, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food

    def walk():
        self.pet.play()
        return self

    def feed():
        self.pet.eat()
        return self
    def bathe():
        self.pet.noise()
        return self
