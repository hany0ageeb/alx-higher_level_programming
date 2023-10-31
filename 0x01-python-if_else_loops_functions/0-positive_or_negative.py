#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if (number > 0):
    msg = f"{number:d} is positive"
elif (number == 0):
    msg = f"{number:d} is zero"
else:
    msg = f"{number:d} is negative"
print(msg)
