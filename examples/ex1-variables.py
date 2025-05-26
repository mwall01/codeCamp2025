import random

amount = random.randint(400, 600)

location = ''
if amount < 475:
    location = 'suburbs'
elif amount < 550:
    location = 'kimmage'
else:
    location = 'harolds'

print(f"Your new amount is: {amount} - buy {location}")

day = 26
month = "May"
temp = 12

day_is_hot = False

if temp > 20:
    day_is_hot = True
    print(f"Today is the {day} of {month} and the temp is {temp}")
else:
    print(f"Today is the {day} of {month} and the temp is {temp}. It is not hot today.")


def your_code():
    
    number = 7

    if number % 2 == 0:
        print("The number is even.")
        return True
    else:
        print("The number is odd.")
        return False
    
your_code()