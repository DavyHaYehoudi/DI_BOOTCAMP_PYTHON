#  Exercise 1 : Temperature Advice
import random


def get_random_temp():
    temp = random.randint(-10, 40)
    return temp


def main():
    tp = get_random_temp()
    if tp < 0:
        print("Brrr, that’s freezing! Wear some extra layers today")
    elif 0 <= tp < 16:
        print("Quite chilly! Don’t forget your coat")
    elif 24 < tp < 32:
        print("It a nice day !")
    else:
        print(f"The temperature right now is {tp} degrees Celsius.")


# main()


def get_random_temp2(season):
    if season == "winter":
        temp = random.randint(-10, 9)
    elif season == "autumn":
        temp = random.randint(10, 16)
    elif season == "spring":
        temp = random.randint(17, 25)
    elif season == "summer":
        temp = random.randint(26, 40)
    else:
        return "It'a not a season"
    return temp


def main2():
    season = input("Choose a season :")
    print(get_random_temp2(season))
# main2()


# Bonus: Give the temperature as a floating-point number instead of an integer.
temp = round(random.uniform(-10, 40), 1)

# Bonus: Instead of asking for the season, ask the user for the number of the month (1 = January, 12 = December). Determine the season according to the month.


def get_random_temp3(month):
    if month == 12 or 1 <= month < 4:
        temp = random.randint(-10, 9)
    elif 4 <= month < 7:
        temp = random.randint(10, 16)
    elif 7 <= month < 10:
        temp = random.randint(17, 25)
    elif 10 <= month < 12:
        temp = random.randint(26, 40)
    else:
        return "It'a not a number of month"
    return temp

def main3():
    month = int(input("Choose a number of month :"))
    print(get_random_temp3(month))
# main3()

# Exercise 2 : When Will I Retire ?
import datetime

def get_age(year, month, day):
    current_year = datetime.datetime.now().year
    current_month = datetime.datetime.now().month
    current_day = datetime.datetime.now().day
    
    age = current_year - year
    if current_month < month or (current_month == month and current_day < day):
        age -= 1
    sexe = input("Enter your gender (M/F) : ")
    if sexe == "M":
        if age >= 67:
            return f'Retirement eligible, {age} years'
        else:
            return f'Retirement not eligible, {67-age} years left'
    elif sexe == "F":
        if age >= 62:
            return f'Retirement eligible, {age} years'
        else:
            return f'Retirement not eligible, {62-age} years left'
    else:
        return 'Invalid gender'

# Exercice 3
def add_numbers(X):
    total = 0
    for i in range(1, 5):
        number = int(str(X) * i)
        total += number
    return total

# Daily Challenge : Exceptions
def divide_by_zero():
    try:
        result = 5 / 0
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")



