#variables
cafe_name = "Oops All Poison"
tax_rate = 0.05 #I lowered taxes to trick people into coming here.

menu = {
    "32 ounces of espresso": 64.00,
    "cafe au poisson": 3.50, #Means "Fish coffee" in French.
    "turkey sandwich": 4.25,
    "turkey* sandwich*": 5.25, #Just a more expensive verison of the Turkey Sandwich. It is against company policy to explain why.
    "s. potion": 2.50, #Looking to randomize this item's price to reflect its behavior in Deltarune, but import is off limits.
    "misery meat": 6.00,
    "mystery meat": 6.00,
    "deuterium oxide": 785.50 #8 oz = 236.588 ml. 236.588 ml of D20 weighs about 262 grams. If I charge $300 per 100 grams (about as much as
}                                        #https://unitednuclear.com/chemicals-metals-c-69/deuterium-oxide-p-135.html charges), then this comes out to about $785.

descriptions = {
    "32 ounces of espresso": "Provides a MASSIVE energy boost! Great for preparing for a big day, or sending you to the hospital so you have an excuse to skip out on said big day.",
    "cafe au poisson": "Authentic French coffee! Nothing's fishy about this item!", 
    "turkey sandwich": "Fresh turkey sandwiches, locally sourced from the nearest hospital.",
    "turkey* sandwich*": "Fresh* turkey* sandwiches*, locally* sourced* from* the* nearest* hospital*.",
    "s. potion": "ITEM ITEM AFFECTS HP A LOT! THE SMOOTH TASTE OF", #Deltarune reference.
    "misery meat": "Meat that's guarunteed to induce a miserable experience.",
    "mystery meat": "Meat that's guarunteed to induce an experience.",
    "deuterium oxide": "It's just like water, but all the hydrogen atoms have an extra neutron, which obviously makes it better. Ethically sourced and zero sugar!\n" +
    "WARNING: ONLY ONE EIGHT OUNCE CUP PER CUSTOMER PER DAY. MORE THAN THAT COULD CAUSE US (even more) LEGAL TROUBLE."
}
order = [] #Note: Throughout the comments, I use "order" and "cart" interchangably. Both refer to this list.

#Functions

#Function for greeting the user and displaying menu options.
#Notably, I will not check for names with weird characters. I figured that an employee here would write anything down as a name.
def greet(name):
    print(
        f"Alright {name}, how can we slightly poison you today?\n\n" +
        "Options:\n" +
        "1: Show Menu\n" +
        "2: Add Item to cart\n" +
        "3: Remove item from cart\n" +
        "4: View Cart\n" +
        "5: Checkout\n" +
        "6: Cancel Order\n"
          )

#Function for printing the menu. Added parameter for description dictionary to print custom item descriptions.
def show_menu(menu, descriptions):
    running_str = "Menu:\n"
    for x in menu:
#For every item in the menu, concatenates the item name, price, and description f strings to running_str, then uses it in one print function.
#I don't actually know if string concatenation is more or less computationally expensive than printing.
#Two line breaks are at the end to separate every item with one empty line.
        running_str = running_str + f"{x.title()}: ${menu[x]:.2f}\nDescription: {descriptions[x]}\n\n" 
    print(running_str)                                               

#Function for showing order. Added parameter for a customizable header. This is so I can use this function in print_receipt() without the order header.
def show_order(order, menu, header:str):
    if order == []: #Sets running_str to an error message and skips the for loop if cart is empty.
        running_str = "You don't have anything in your cart, goober."
    else:
        running_str = header
        for x in order:
            running_str = f"{running_str}{x.title()}: ${menu[x]:.2f}\n" #Adds every item to the running string and its price
        running_str = f"{running_str}Items: {len(order)}\n" #Adds total item quantity to running_str
    print(running_str) #Prints running string.
        

#Function for calculating subtotal. Returns a number.
def calculate_subtotal(order, menu):
    running_total = 0 #Intializes running_total
    for x in order:
        running_total += menu[x] #Adds the price of every item in the order to the running total, then returns it.
    return running_total

#Function for calculating discounts. Returns a number.
def get_discount(subtotal:float, is_member:bool):
    if is_member and subtotal >= 20: #Discount is %15 with membership and a cart with more than $20.
        return subtotal * 0.15
    elif is_member and subtotal >= 10: #Discount is %10 with membership and a cart with between $10-20 (20 exclusive).
        return subtotal * 0.10
    elif not is_member and subtotal >= 25: #Discount is %5 without membership and a cart with more than $25.
        return subtotal * 0.05
    else: #If ineligible for discounts.
        return 0.00

#Function for printing receipt. Returns True if cart isn't empty to let the program know to stop later on.
def print_receipt(name, order, menu, is_member):
    show_order(order, menu, f"===== {cafe_name} RECEIPT =====\nVictim: {name}\n") #Uses show order to print most of the receipt. Victim name is part of the header.
    if order == []: #Skips following code and returns False if order is empty.
        return False
#Price math
    subtotal = calculate_subtotal(order, menu)
    tax = subtotal * tax_rate
    discount = get_discount(subtotal + tax, is_member)
    total = (subtotal - discount) + tax
    print(f"Subtotal: ${subtotal:.2f}\nDiscount: ${discount:.2f}\nTax: ${tax:.2f}\nTotal: ${total:.2f}\n") #Prints price stuff
    if not is_member:
        print("Consider becoming a rewards member to get up to %15 your next purchase! Please. I beg you.")
    return True

def add_to_order(item:str, quantity:int, order:list):
    if quantity < 1: #Cancels order if input is 0. Exits function so the success message doesn't show.
        print("Nothing was added to your order.")
        return
    for x in range(quantity): #Adds quantity items to order.
        order.append(item)
    print(f"Added {quantity} {item.title()}(s) to your cart.") #Success message.

#Prompts user to input something, and prompts them again if their choice isn't in the give list.
def list_select(prompt:str, options:list, fail_prompt:str):
    user_input = input(prompt).lower()#Makes the input lowercase
    while True:
        if user_input.isdigit(): #Converts input to numbers if the input is only made up of numbers 0-9.
            user_input = int(user_input)
        if user_input in options: #Returns input if it's in the list.
            return user_input
            break
        else:
            user_input = input(fail_prompt).lower() #Prompts again if input is invalid. Makes input lowercase as well.

#Runs list select with a predefined "y or n" list, then returns True if input is yes or y, otherwise it returns False.
def y_or_n(prompt:str):
    user_input = list_select(prompt, ["yes", "y", "no", "n"], "Yes or No?")
    if user_input == "yes" or user_input == "y":
        return True
    else:
        return False

#Variation of list select that prompts the user to pick a number in the option range. Second parameter should be a list of only numbers, ideally generated by range().
def number_select(prompt:str, option_range:list):
    return list_select(prompt, option_range, f"Please enter a number {option_range[0]}-{option_range[-1]}: ")

#stack
customer_name = input(f"Hello, welcome to {cafe_name}. Can I get a name for your order?: ") #Gets name
memberstatus = y_or_n("Are you a rewards member? (yes (or y)/ no (or n): ") #Gets member status
greet(customer_name) #Greets customer

while True:
    user_input = number_select(f"Please select an option (1-6): ", range(1, 7)) #Prompts user to pick a number from 1-6.
#Uses given input to perform selected action

#Shows menu.
    if user_input == 1:
        show_menu(menu, descriptions)

#Adds item to the menu.
    elif user_input == 2:
        item = list_select("Please select an item from the menu: ", menu.keys(), "Sorry, that's not on the menu. Please pick something else: ") #Uses menu keys for the list
#Prompts you to select quantity if your selection wasn't deuterium oxide.
        if item != "deuterium oxide":
#Caps number of items you can buy at once to 100, if you're not trying to buy deuterium oxide.
#This is because I couldn't figure out how to allow the number_select function to let the user pick numbers from 0 to inf, and didn't want to make a new function for that.
            quantity = number_select("Please select how many of this item you want. Enter 0 to cancel: ", range(101))
            add_to_order(item, quantity, order)
#Code that stops you from having more than one deuterium oxide cup.
        elif item in order:
            print("Sorry, only one per customer.")
        elif y_or_n("Are you sure you want to add one cup of Deuterium Oxide? Only one per customer. (y/n): "): #Adds one Deuterium oxide if the customer has none and says yes.
            add_to_order("deuterium oxide", 1, order)

#Removes item from cart.
    elif user_input == 3:
        if order == []: #Checks if cart is empty, and prints an error message if it is.
            print("You don't have anything in your cart, goober.")
        else:
            item = list_select("Please select an item from your cart: ", order, "That's not in your cart. Please pick something else: ")
            quantity = number_select(f"How many {item.title()}s would you like to remove? Type 0 to cancel: ", range(0, order.count(item) + 1)) #Finds out how many of the choosen item exist in the cart, and uses that as the maxium amount you can remove.
            for x in range(quantity): #Removes quantity number of the item and prints success message.
                order.pop(order.index(item))
            print(f"Removed {quantity} {item.title()}(s) from your cart")

#Prints everything in the cart. Prints a special message if nothing is in there.
    elif user_input == 4:
        show_order(order, menu, "--- YOUR ORDER ---\n")

#Prints receipt.
    elif user_input == 5:
        if print_receipt(customer_name, order, menu, memberstatus): #Prints receipt and closes the program (if order isn't empty)
            print(f"Thanks for shopping at {cafe_name}! Have an great rest of your day! Or not. That's not really within our control.")
            break

#Asks for confirmation. If the user confirms, cancel the order and close the program.
    elif user_input == 6:
        if y_or_n("Are you sure you want to cancel your order? (y/n): "):
            print("Order cancelled.")
            break

#Failsafe in case user_input is somehow set to something invalid. Theoretically, this shouldn't happen, but if it does, I don't want the program crashing.
    else:
        print("Congrats, you broke something. Ending program.")
        break
