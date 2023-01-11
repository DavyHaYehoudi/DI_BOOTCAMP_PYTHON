# Exercise 1 : Human
from typing import List


class Human:
    def __init__(self, name: str, age: int, living_place=None):
        self.name = name
        self.age = age
        self.living_place = living_place

    def move(self, building):
        self.living_place = building
        building.inhabitants.append(self)


class Building:
    def __init__(self, address: str, inhabitants: List[Human] = []):
        self.address = address
        self.inhabitants = inhabitants


class City:
    def __init__(self, name: str, buildings: List[Building] = []):
        self.name = name
        self.buildings = buildings

    def construct(self, address: str):
        self.buildings.append(Building(address))

    def info(self, address: str):
        building = next(
            (b for b in self.buildings if b.address == address), None)
        if building:
            print(f'Number of buildings: {len(self.buildings)}')
            age = [i.age for i in building.inhabitants]
            if len(age) > 0:
                print(f'Mean age of citizens: {sum(age) / len(age)}')
            else:
                print("This building is empty")
        else:
            print(f'No building found at this address: {address}')


# Creating objects
human1 = Human('John', 25)
human2 = Human('Jane', 30)
building1 = Building('Street 1')
building2 = Building('Street 2')
city = City('Paris')

human1.move(building1)
human2.move(building1)
city.construct(building1.address)
city.construct(building2.address)
city.info(building1.address)
city.info

# Daily Challenge : Food


class Person():
    def __init__(self, name, like, hate):
        self.name = name
        self.like = like
        self.hate = hate

    def taste(self, food):
        x = "!"
        if food in self.like:
            x = "and loves it"
        if food in self.hate:
            x = "and hates it"
        return f'{self.name} eats the {food} {x} '


p1 = Person("Sam", ["ice cream"], ["carrots"])
print(p1.taste("ice cream"))
print(p1.taste("cheese"))
print(p1.taste("carrots"))
