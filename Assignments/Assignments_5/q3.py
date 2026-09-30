#Sorry I couldn't come up with something more creative to add to this. I wanted to also check the primality of the inputted number,
#but doing that effeciently requires more coding and math skills than I currently have.

#Checks the parity of the inputted integer.
def check_number(number:int):
    if round(number / 2) == number / 2: #ex: 4/2 = 2, which when rounded still equals 2, and thus 4 is even.
        return "even"
    else:                                    #ex: 3/2 = 1.5, which when rounded does not equal 1.5, and thus 3 is odd.
        return "odd"

#First prompt
user_input = input("Please enter an integer:")

#Main loop
while True:
    try:
        parity = check_number(int(user_input))         #Tries to turn the user's input into an integer. If it succeeds, it'll store the parity in a variable,
        print(f"{user_input} is an {parity} number.")  #print the inputted number and parity in this f string,
        break                                          #then exit the loop.
    except:                                            #Otherwise, instead of crashing, it'll just ask again.
        user_input = input("That was not an interger, please try again.") #Subsequent prompts
