#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_d = abs(number) % 10

if number < 0:
    last_d = -last_d

if last_d >= 6:
    print(f"Last digit of {} is {} and greater than 5".format(number, last_d))

elif last_d == 0:
    print(f"Last digit of {} is {} and is 0".format(number, last_d))

else:
    print(f"Last digit of {} is {} and is less than 6 and not 0".format(number, last_d))
