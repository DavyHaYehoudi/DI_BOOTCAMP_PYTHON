 # Exercise 1: Cats
class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age


kiwee = Cat("Kiwee", 15)
felix = Cat("Felix", 7)
minet = Cat("Minet", 3)

cats = [kiwee, felix, minet]


def find_the_oldest(cats):
    oldest_age = 0
    for cat in cats:
        if cat.age > oldest_age:
            oldest_age = cat.age
            oldest_name = cat.name
    print(f"The oldest cat is {oldest_name}, and is {oldest_age} years old.")


find_the_oldest(cats)

#  Exercise 2 : Dogs
class Dog():
    def __init__(self,name,height):
        self.name = name
        self.height = height
    
    def bark(self):
        print(f"{self.name} goes woof!")
    
    def jump(self):
        print(f"{self.name} jumps {self.height*2}cm high !")

davids_dog = Dog("Rex",50)
print(davids_dog.bark())
print(davids_dog.jump())

sarahs_dog = Dog("Teacup",20)
print(sarahs_dog.bark())
print(sarahs_dog.jump())

if davids_dog.height > sarahs_dog.height:
    print(f"{davids_dog.name} is bigger than {sarahs_dog.name}")
else:
    print(f"{sarahs_dog.name} is bigger than {davids_dog.name}") 
 
# Exercise 3 : Who’s The Song Producer?
class Song():
    def __init__(self,lyrics):
        self.lyrics = lyrics
    
    def sing_me_a_song(self):
        for word in self.lyrics:
            print(f"{word}")

stairway = Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])
stairway.sing_me_a_song()

# Exercise 4 : Afternoon At The Zoo
class Zoo():
    def __init__(self,animals,name):
        self.animals = animals
        self.name = name
    
    def add_animals(self,new_animal):
        if self.animals.count(new_animal)==0:
            self.animals.append(new_animal)
    
    def get_animals(self):
        for animal in self.animals:
            print(f"{animal} ")

    def sell_animal(self,animal_sold):
        if self.animals.count(animal_sold):
            self.animals.remove(animal_sold)
        else :
            print("this animal doesn't exist in our zoo")

    def sort_animals(self):
        print(self.animals.sort())

    # Daily Challenge: Old MacDonald’s Farm
class Farm:
    def __init__(self, name):
        self.name = name
        self.animals = {}

    def add_animal(self, animal_type, count=1):
        if animal_type in self.animals:
            self.animals[animal_type] += count
        else:
            self.animals[animal_type] = count

    def get_info(self):
        info = f"{self.name}'s farm\n"
        for animal, count in self.animals.items():
            info += f"{animal:<6} : {count}\n"
        return info + "E-I-E-I-O!"

macdonald = Farm("McDonald")
macdonald.add_animal('cow',5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())
