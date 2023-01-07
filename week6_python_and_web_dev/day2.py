# Exercise 1 : Hello World
import random
for x in range(4):
    print("Hello world")

# Exercise 2 : Some Math
result = 99**3*8
print(result)

# Exercise 3 : What Is The Output ?
print(5 > 3)  # True
print(3 == 3)  # True
print(3 == "3")  # False
print("3" > 3)  # TypeError: '>' not supported between instances of 'str' and 'int'
print("Hello" == "hello")  # False

# Exercise 4 : Your Computer Brand
computer_brand = "Lenovo"
print(f"I have a {computer_brand} computer")

# Exercise 5 : Your Information
name = "Davy"
age = 44
shoe_size = 44
info = f"My name is {name}, I am {age}, my shoe_size is {shoe_size} and I love programming"
print(info)

# Exercise 6 : A & B
a = 10
b = 1
if a > b:
    print('Hello World')

# Exercise 7 : Odd Or Even
number = input("Let choose a number : ")
print(f"Your number {number} is odd" if int(number) %
      2 != 0 else f"Your number {number} is even")

# Exercise 8 : What’s Your Name ?
name = input("What is your name ?")
print("Your name is different from mine, dont'y worry, nobody is perfect !" if name !=
      "Davy" else "What a great name !")

#  Exercise 9 : Tall Enough To Ride A Roller Coaster
height = input("How tall are you in inches ?")
print("You are tall enough to ride" if int(height)
      > 145 else "You need to grow some more Bro !")

# Daily Challenge: Build Up A String

# Using the input function, ask the user for a string. The string must be 10 characters long.
# If it’s less than 10 characters, print a message which states “string not long enough”.
# If it’s more than 10 characters, print a message which states “string too long”.

word = "ReallyMans"
nbr_char = len(word)
if nbr_char == 10:
    print("Perfect")
elif nbr_char > 10:
    print("string too long")
elif nbr_char < 10:
    print("string not long enough")

    # Then, print the first and last characters of the given text.
first_char = word[0]
last_char = word[-1]
print(
    f"The first character of the string is the letter {first_char} and the last character is the letter {last_char} ")

# Using a for loop, construct the string character by character: Print the first character, then the second, then the third, until the full string is printed
word_concac = ""
for letter in word:
    word_concac += letter
    print(word_concac)

    # . Bonus: Swap some characters around then print the newly jumbled string (hint: look into the shuffle method)
list_word = list(word)
random.shuffle(list_word)
new_word = "".join(list_word)
print(new_word)
