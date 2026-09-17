import random

#Randomized grades to be between 70-100. Because Kevin is an idiot, his grade is randomized between 0-50.
John = random.randint(70, 100)
Susan = random.randint(70, 100)
Kevin = random.randint(0, 50)

classroom = [John, Susan, Kevin]

#Function that calculates average. Input must be a list.
def average(classavg: list):
    runningtotal = 0
    for x in classavg:
        runningtotal += x
    return round(runningtotal / len(classavg), 2)

classaverage = average(classroom)
#Prints class average
print(f"The class average for the last test was {classaverage}%!")