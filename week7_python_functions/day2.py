# Exercise 1 : What Are You Learning ?
def display_message():
    name = input("your name ? :")
    print(f"I am learning functions in Python language {name} ")
display_message()

# Exercise 2: What’s Your Favorite Book ?
def favorite_book(title):
    print(f"One of my favorite books is {title} ")
favorite_book("Conversations with God")

# Exercise 3 : Some Geography
def describe_city(city,country="France"):
    print(f"{city} is in {country} ")
describe_city("Paris")

# Exercise 4 : Random
import random
x = random.randint(1,100)
def rdm(x):
    y = random.randint(1,100)
    if(x==y):
        print("Success, it's the same number !")
    else:
        print(f"Fail, the numbers were : {x} and {y} ")
rdm(52)

#  Exercise 5 : Let’s Create Some Personalized Shirts !
def make_shirt(size = "large", text="I love Python" ):
    print(f"The size of the shirt is {size} and the text is {text} ")
make_shirt()
make_shirt(size= "medium")
make_shirt(size="anysize",text="a different message")

# Exercise 6 : Magicians …
magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
def show_magicians(magician_names):
    for name in magician_names:
        print(name)


def make_great(magician_names):
    for name in magician_names:
        print(f"{name} the Great")
make_great(magician_names)
show_magicians(magician_names)

# Daily Challenge: Solve The Matrix
matrix = [
    "7i3",
    "Tsi",
    "h%x",
    "i #",
    "sM",
    "$a",
    "#t%",
    "^r!"
]

# Create a list of lists where each inner list represents a column in the matrix
columns = []
for i in range(len(matrix[0])):
    columns.append([row[i] for row in matrix])

# Create a list of strings where each string is the alpha characters in a column
alpha_columns = []
for column in columns:
    alpha_columns.append(''.join([c for c in column if c.isalpha()]))

# Concatenate the strings in alpha_columns and add a space between each group of symbols
secret_message = ''
i = 0
while i < len(alpha_columns[0]):
    for column in alpha_columns:
        if i < len(column):
            secret_message += column[i]
        else:
            break
    secret_message += ' '
    i += 1

print(secret_message)
