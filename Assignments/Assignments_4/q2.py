import math

#Given values
length = 12.5
width = 4

#Solved-for values
area = round((length * width), 2)
perimeter = round((2 * length) + (2 * width), 2)

#lil extra
diagonal = round(math.sqrt((length ** 2) + (width ** 2)), 2)

#print values
print(f"The area of this rectangle is {area}, the perimeter of this rectangle is {perimeter}, and the diagonal of this rectangle is {diagonal}.")