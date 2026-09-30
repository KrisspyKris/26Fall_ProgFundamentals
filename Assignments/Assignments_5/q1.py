#List of characters that'll will considered invalid.
invalidcharacters = [
        #v Instead of quotation marks, uses apostrophes to avoid an error when storing quotation marks.
    "!", '"', "#", "$", "%", "&", "(", ")", "*", "+", ",", ".", "/", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
    ":", ";", "<", "=", ">", "?", "@", "[", "\\", "]", "^", "_", "`", "{", "|", "]", "~",
    ]                                        #^Uses two backslashes because \ is the escape character, and will make the program
#think the following quotation marks and commas are part of the same string. Two backslashes stops the escape and results in a string with only one backslash.
          
def greet_user(name:str):   #Function mandated by the assignment that prints the name passed into the function.
    print(f"Hello, {name}! Welcome aboard!") #Welcome aboard what?!

#Checks if the inputted string has any of the invalid characters, is an empty string, or is all spaces.
#Returns False if the string is invalid, otherwise it returns True.

def is_validusername(username:str):
#Checks if the string is all spaces or is an empty string.
    if username.isspace() == True or username == "":
        return False
    for x in invalidcharacters:
#username.find(x) returns -1 if the string does not contain 'x', otherwise, it returns the position of the first occurence of 'x'.
#This means that if I for-loop through the invalidcharacters list, and username.find(x) returns anything other than -1,
#we know the string is invalid because it contains an invalid character.
        if username.find(x) != -1:    
            return False
#Returns True if the string passes all the checks.
    return True

#First time the program asks the user for a name.
userInputName = input("Please enter your name!: ")

while True:
#Greets the user once a valid name is choosen using a capitalized verison of the name, then breaks out of the while loop and ends the program.
    if is_validusername(userInputName) == True:
        greet_user(userInputName.title())
        break
    else:
#Lightly pokes fun at the user if they insert an invalid name and prompts them to try again.
#This message will keep appearing until a valid name is choosen because of the while loop.
        userInputName = input("I somehow doubt that's your name. Please try again: ")

