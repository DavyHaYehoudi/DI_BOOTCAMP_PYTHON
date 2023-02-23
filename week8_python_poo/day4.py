# Exercise 1 : Pets
class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())


class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'


class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Siamese(Cat):
    pass


bengal = Bengal("Ben", 5)
chartreux = Chartreux("Char", 6)
siamese = Siamese("Siam", 7)

all_cats = [bengal, chartreux, siamese]
sara_pets = Pets(all_cats)

print(sara_pets.walk())

# Exercice 2 : Chiens


class Dog():
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        print(f"{self.name} is barking")

    def run_speed(self):
        speed = self.weight/self.age*10
        return speed

    def fight(self, other_dog):
        my_power = self.run_speed() * self.weight
        other_power = other_dog.run_speed() * other_dog.weight
        if my_power > other_power:
            return f"{self.name} won the fight"
        else: # this else it's redundant bucause you do return at the if statment
            return f"{other_dog.name} won the fight"


dog1 = Dog("Fido", 3, 15)
dog2 = Dog("Buddy", 4, 25)
dog3 = Dog("Rocky", 5, 35)

# Exercise 3 : Dogs Domesticated


class PetDog(Dog):
    def __init__(self, name, age, weight, trained=False):
        super().__init__(name, age, weight)
        self.trained = trained

    def train(self):
        print(self.bark())
        self.trained = True

    def play(self, *args):
        dog_names = " ".join(args)
        print(f"{dog_names} all play together")

# Exercise 1 : Family
class Family:
    def __init__(self, last_name):
        self.last_name = last_name
        self.members = [
            {'name':'Michael','age':35,'gender':'Male','is_child':False},
            {'name':'Sarah','age':32,'gender':'Female','is_child':False}
        ]
        
    def born(self, **kwargs):
        kwargs["is_child"] = True
        self.members.append(kwargs)
        print(f"Congratulations to the {self.last_name} family on the birth of their new child!")
        
    def is_18(self, name):
        for member in self.members:
            if member["name"] == name:
                if member["age"] >= 18:
                    return True
                else: # this else it's redundant bucause you do return at the if statment
                    return False
        return None # Why to return None? and not default value which is False
    
    def family_presentation(self):
        print(f"Meet the {self.last_name} family:")
        for member in self.members:
            print(f" - {member['name']} {self.last_name}")

# Exercise 2 : TheIncredibles Family...

# Daily Challenge : Pagination...
