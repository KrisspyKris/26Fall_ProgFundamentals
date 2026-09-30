#Calculates a rectangle's area and perimeter based on given length and width. The two parameters can be either floats or integers.
def rectangle_stats(length, width):
    area = length * width
    perimeter = (2 * length) + (2 * width)
    return area, perimeter #Returns two numbers

def str_to_floats(input:str):
    split_input = input.split(" ", 1) #Splits the input string at the first space and puts both strings into a list.
    try:                             #Attempts to convert the two elements of the list into floats.
        return float(split_input[0]), float(split_input[1])
    except:                          #Returns False instead of crashing if the strings cannot become floats.
        return False          
#First time the user is prompted for input
user_input = input(
    "Please enter two numbers separated by one space to define a rectangle's lenght and width.\n" +
    "Example: 7 4\n"
                   )
#Main while loop, done so the program can endlessly prompt the user again until a valid input is given.
while True:
    if str_to_floats(user_input) == False: #Prompts the user for input again if the last input was invalid.
        user_input = input("Invalid input, please try again:\n")
    else:
        length, width = str_to_floats(user_input) #Puts the output of str_to_floats into two variables if the input was valid.
        area, perimeter = rectangle_stats(length, width) #Puts the output of rectangle_stats into two variables.
        print("Area: {:.2f}, Perimeter: {:.2f}".format(area, perimeter)) #Prints the area and perimeters after rounding, then closes the program.
        break
    
