import math
name = "Alice"
age = 21
meters = 1.75 #in meters

feet = math.floor(meters * 3.281)
inches = round((meters * 39.37) % 12)

print(f"{name} is {age} years old and {meters} meters tall, or in good ol' murican units, {feet} foot {inches} inches.")