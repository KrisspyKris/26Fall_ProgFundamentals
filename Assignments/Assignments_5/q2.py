#Calculates a rectangle's area and perimeter based on given length and width. The two parameters can be either floats or integers.
def rectangle_stats(length, width):
    area = length * width
    perimeter = (2 * length) + (2 * width)
    return area, perimeter #Returns two numbers

#First time the user is prompted for input
user_input = input(
    "Please enter two numbers separated by one space to define a rectangle's lenght and width.\n" +
    "Example: 7 4\n"
                   )
#Main while loop, done so the program can endlessly prompt the user again until a valid input is given.
while True:
    split_input = user_input.split(" ", 1) #Splits the input string at the first space and puts both strings into a list.
    try:
        length, width = float(split_input[0]), float(split_input[1]) #Tries to turn the split strings into floats.
#If the float functions succeeds:
        area, perimeter = rectangle_stats(length, width) #Puts the output of rectangle_stats into two variables.
        print("Area: {:.2f}, Perimeter: {:.2f}".format(area, perimeter)) #Prints the area and perimeters after rounding, then closes the program.
        break
    except:
        user_input = input("Invalid input, please try again:\n") #Prompts the user for input again instead of crashing if the user input could not be split into floats.
    
