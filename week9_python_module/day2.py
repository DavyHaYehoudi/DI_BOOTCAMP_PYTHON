# Exercise 1: Import
import func
func.add(5,6)

# Exercise 2: Random Module
import random
def rdm(x):
    y = random.randint(1,100)
    if x==y:
        print("success !")
    else :
        print("failed")
rdm(12)

# Exercise 3: String Module
"???"

# Exercise 4 : Current Date
from datetime import datetime, timedelta

def date_today():
    print(datetime.now().date())
date_today()

# Exercise 5 : Amount Of Time Left Until January 1st
def time_until_jan1():
    current_time = datetime.now()
    next_jan1 = datetime(year=current_time.year+1, month=1, day=1)
    time_left = next_jan1 - current_time
    print(f'Time left until January 1st is {time_left}')
time_until_jan1()

# Exercise 6 : Birthday And Minutes
from datetime import datetime

def calculate_age_in_minutes(birthdate:str):
    birthdate_dt = datetime.strptime(birthdate, '%Y-%m-%d')
    current_time = datetime.now()
    age = current_time - birthdate_dt
    age_minutes = age.total_seconds() / 60
    print(f'You have lived {age_minutes:.0f} minutes.')

calculate_age_in_minutes('1995-07-25')

# Exercise 7 : Upcoming Holiday
from datetime import datetime, timedelta

def next_holiday():
    current_time = datetime.now()
    print("Today's date is:", current_time.date())
    
    holiday_date = datetime(year=current_time.year, month=12, day=25) 
    if holiday_date < current_time: 
        holiday_date = holiday_date.replace(year=current_time.year+1) 
    
    time_left = holiday_date - current_time
    print(f'Time left until the next holiday is {time_left}')
    print("The next holiday is Christmas")

next_holiday()


