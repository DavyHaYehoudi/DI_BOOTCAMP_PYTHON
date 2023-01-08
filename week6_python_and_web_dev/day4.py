""" #  Exercise 1 : Set
my_fav_numbers = {0,1,2,3,5,7,10,33,45}
my_fav_numbers.update([22,55])
my_fav_numbers.remove(55)
# print(my_fav_numbers)

friend_fav_numbers = {100,99,98,97,96,95}

our_fav_numbers1 = my_fav_numbers | friend_fav_numbers
print(our_fav_numbers1)
# OR
our_fav_numbers2 = my_fav_numbers.union(friend_fav_numbers)
print(our_fav_numbers2)

# Exercise 2: Tuple
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
tuple3 = tuple1 + tuple2

# Exercise 3: List
basket = ["Banana", "Apples", "Oranges", "Blueberries"]

basket.remove("Banana")
basket.remove("Blueberries")
basket.append("Kiwi")
basket[0] = "Apples"
basket.count("Apples")
basket.clear()
print(basket)

# Exercise 4: Floats
    # A float is a type variable of Python langage. The difference between an integer and a float that's the float type is a decimal number and not a entire number as integer.
import numpy as np
floats = np.arange(1.5, 5, 0.5)
print(floats)

# Exercise 5: For Loop
list=[]
for n in range(1,21):
    list.append(n)
print(list)

list_even=[]
for n in range(1,21):
    if n%2 == 0:
        list_even.append(n)
print(list_even)

# Exercise 6 : While Loop
my_name = "Davy"
his_name = input("What's your name ?")
while his_name != my_name:
    print("No, its's not my name")
    break

# Exercise 7: Favorite Fruits
fruits = input("Tell us your favorite fruits are :")
list=[]
for fruit in fruits.split(" "):
    list.append(fruit)

fruit_user = input("Tape a name of any fruit :")
if fruit_user in list:
    print("You chose one of your favorite fruits! Enjoy!")
else :
    print("You chose a new fruit. I hope you enjoy")

# Exercise 8: Who Ordered A Pizza ?
toppings_list=[]

while True:
    toppings_choice = input("Choose a topping or tape quit to finish :")
    if toppings_choice == "quit":
        all_topings=""
        for topping in toppings_list:
            all_topings += topping +", "
        print(f"You have choose the pizza pie with all those toppings : {all_topings} and the price is 10$ + 2.5$ for each topping so the total is {topping_price} $")
        break
    else :
       toppings_list.append(toppings_choice)
       topping_price = len(toppings_list)*2.5 + 10
       print(f"you ll add {toppings_choice} to your pizza")

# Exercise 9: Cinemax
ctg_price = (0, 10, 15)
list_watchers = []
list_restricted = ["tuner", 'robots', "aligator"]

cost = 0
while True:
    name = input("What's your name ? :")
    moovie = input("For which moovie ? :")
    age = input("How old are you (or quit if you finished) ? : ")
    if age != "quit":
        age = int(age)
    if age != "quit" and 3 < age < 12:
        cost += ctg_price(1)
    elif age != "quit" and age >= 12:
        cost += ctg_price(2)
    elif moovie in list_restricted and 16 < age < 21:
        list_watchers.append(name)
    elif age == "quit":
        print(f"The total cost for your family is {cost} $")
        break """

# Exercise 10 : Sandwich Orders
sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]
finished_sandwiches = []

for sdw in sandwich_orders:
    finished_sandwiches.append(sdw)
    print(f"I made your {sdw} ")

# Exercise 11 : Sandwich Orders#2
pastrami_times = sandwich_orders.count("Pastrami sandwich")
if pastrami_times >=3:
    print("it's ok for the pastrami !")
else :
    print("the pastrami doesn't appear 3 times...")

print("the deli has run out of pastrami")
while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")
while "Pastrami sandwich" in finished_sandwiches[-1] :
    finished_sandwiches.pop()