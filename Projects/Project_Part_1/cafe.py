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
main_menu = ("Options:\n" +
        "1: Show Menu\n" +
        "2: Add Item to cart\n" +
        "3: Remove item from cart\n" +
        "4: View Cart\n" +
        "5: Checkout\n" +
        "6: Cancel Order\n" +
        "Please select an option (1-6): ")


#Functions
#Unlike my work in assignment 5, I will not check for names with weird characters. I figured that an employee here would write anything down as a name.
def greet(name):
    print(f"Alright {name}, how can we slightly poison you today?")

def show_menu(menu):
    running_str = "\nMenu:\n"
    for x in menu:
#For every item in the menu, concatenates the item name, price, and description to running_str, then uses it in one print function.
#Two line breaks are at the end to separate every item with one empty line.
        running_str = running_str + f"{x}: ${menu[x]:.2f}\nDescription: {descriptions[x]}\n\n"
    print(running_str)                                               

#Shows the header followed by every item in the order, then followed by an item total if item_total is True. If the order is empty, only an error message will show.
def show_order(order, menu, header, item_total):
    if does_order_have_items(order):
        running_str = header #Intializes temporary variable as the header.
        for x in order:
            running_str = f"{running_str}\n{x}: ${menu[x]:.2f}" #Adds every item to the running string and its price
        if item_total:
            running_str = f"{running_str}\nItems: {len(order)}\n"
        print(running_str) #Prints running string.

#Returns a number.
def calculate_subtotal(order, menu):
    running_total = 0 #Intializes running_total
    for x in order:
        running_total += menu[x] #Adds the price of every item in the order to the running total, then returns it.
    return running_total

#Returns a number.
def get_discount(subtotal, is_member):
    if is_member and subtotal >= 20: #Discount is %15 with membership and a cart with more than $20.
        return subtotal * 0.15
    elif is_member and subtotal >= 10: #Discount is %10 with membership and a cart with between $10-20 (20 exclusive).
        return subtotal * 0.10
    elif not is_member and subtotal >= 25: #Discount is %5 without membership and a cart with more than $25.
        return subtotal * 0.05
    else: #If ineligible for discounts.
        return 0.00

def print_receipt(name, order, menu, is_member):
#Price math
    subtotal = calculate_subtotal(order, menu)
    tax = subtotal * tax_rate
    discount = get_discount(subtotal, is_member)
    total = (subtotal - discount) + tax
    footnote = f"Subtotal: ${subtotal:.2f}\nDiscount: ${discount:.2f}\nTax: ${tax:.2f}\nTotal: ${total:.2f}\n" #Sets footnote to string containing price info
    if not is_member:
        footnote = f"{footnote}Consider becoming a rewards member to get up to %15 your next purchase! Please. I beg you.\n" #Adds membership ad to footnote if is_member is False.
    footnote = f"{footnote}\nThanks for shopping at {cafe_name}! Have an great rest of your day! Or not. That's not really within our control." #Adds goodbye message to footnote
    show_order(order, menu, f"\n===== {cafe_name} RECEIPT =====\nVictim: {name}", False) #Prints receipt
    print(footnote) #Prints footnote.

def add_to_order(item, quantity, order):
    if quantity < 1: #Cancels order if input is 0 and shows cancel message.
        print("Nothing was added to your order.\n")
        return
    for x in range(quantity): #Adds quantity items to order.
        order.append(item)
    print(f"Added {quantity} {item}(s) to your cart.\n") #Success message.

#Custom functions
#Returns True if it does, otherwise it returns False and prints an error. Since I check this multiple times in the program, I'd thought I'd make it its own function.
def does_order_have_items(order):
    if order != []:
        return True
    print("You don't have anything in your cart, goober.\n")
    return False

#Prompts user to input something, and prompts them again if their choice isn't in the give list.
def list_select(prompt, options, fail_prompt):
    user_input = input(prompt).lower()#Makes the input lowercase
    while True:
        if kn_is_digit(user_input): #Converts input to numbers if the input is only made up of numbers 0-9.
            user_input = int(user_input)
        if user_input in options: #Returns input if it's in the list.
            return user_input
            break
        else:
            user_input = input(fail_prompt).lower() #Prompts again if input is invalid. Makes input lowercase as well.

#Runs list select with a predefined "y or n" list, then returns True if input is yes or y, otherwise it returns False.
def y_or_n(prompt):
    user_input = list_select(prompt, ["yes", "y", "no", "n"], "Yes or No?: ")
    if user_input == "yes" or user_input == "y":
        return True
    else:
        return False

#Variation of list select that prompts the user to pick a number in the option range. Second parameter should be a list of only numbers, ideally generated by range().
def number_select(prompt, option_range):
    return list_select(prompt, option_range, f"Please enter a number {option_range[0]}-{option_range[-1]}: ")
#option_range[-1] is the last item in the list. If the list was generated with range(), this should be the largest number.

#"Knock-off" versions of string/list methods not avaible in Module 5.
#I wanted to include .title(), but determined that it'd be too annoying to make for a small cosmetic change.
def kn_is_digit(string):
#Returns False if string is empty
    if string == "":
        return False
    digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
#Loops through all letters in string, and returns False if any of them aren't numbers. If it gets through the whole string, return True.
    for x in string:
        if x not in digits:
            return False
    return True

#Loops through the given list and increments count by 1 for each of a specified item it finds, then returns count.
def kn_count(input_list, item):
    count = 0
    for x in input_list:
        if x == item:
            count += 1
    return count

#main loop
customer_name = input(f"Hello, welcome to {cafe_name}. Can I get a name for your order?: ") #Gets name
greet(customer_name) #Greets customer
memberstatus = y_or_n(f"Are you a rewards member? (yes (or y)/ no (or n): ") #Gets member status

while True:
    user_input = number_select(main_menu, range(1, 7)) #Prompts user to pick a number from 1-6.
#Uses given input to perform selected action

#Shows menu.
    if user_input == 1:
        show_menu(menu)

#Adds item to the order.
    elif user_input == 2:
        item = list_select("What from the menu would you like to add?: ", menu.keys(), "Sorry, that's not on the menu. Please pick something else: ") #Uses menu keys for the list
        quantity = 0 #Default value for quantity. If D20 is in the order, or if the user refuses to buy it, this will stay at 0.
        if item != "deuterium oxide":
#Caps number of items you can buy at once to 100, if you're not trying to buy deuterium oxide.
#This is because I couldn't figure out how to allow the number_select function to let the user pick numbers from 0 to inf, and didn't want to make a new function for that.
#As a bonus, this stops someone from ordering billions of items at once, causing the program to hog tons of computer resources!            
            quantity = number_select("Please select how many of this item you want. Enter 0 to cancel: ", range(101))
#Code that stops you from having more than one deuterium oxide cup.
        elif item in order:
            print("Sorry, only one per customer.")
        elif y_or_n("Are you sure you want to add one cup of Deuterium Oxide? Only one per customer. (y/n): "): #Adds one Deuterium oxide if the customer has none and says yes.
            quantity = 1
        add_to_order(item, quantity, order)

#Removes item from cart.
    elif user_input == 3:
#Finds out how many of the choosen item exist in the cart, and uses that as the maxium amount you can remove.
        if does_order_have_items(order):
            item = list_select("Please select an item from your cart: ", order, "That's not in your cart. Please pick something else: ")
            quantity = number_select(f"How many {item}s would you like to remove? Type 0 to cancel: ", range(0, kn_count(order, item) + 1))
            for x in range(quantity):
                order.remove(item) #Removes the first instance of item to be removed quantity times.
            print(f"Removed {quantity} {item}(s) from your cart.") #Success message

#Prints everything in the cart.
    elif user_input == 4:
        show_order(order, menu, "\n--- YOUR ORDER ---", True) #Calls show order with item_total set to True.

#Prints receipt.
    elif user_input == 5:
        if does_order_have_items(order):
            print_receipt(customer_name, order, menu, memberstatus)
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
