#Oh no! Steve broke out of a fifth grade math problem and went to Walmart to buy 20 watermelons and 13 oranges!
#This is his cart and the items' prices.
cart = {"watermelon" : 20, "orange" : 13}
prices = {"watermelon" : 4.13, "orange" : 1.35}

#5% tax rate
taxrate = .05

#Subtotals are separated by item type so that an itemized receipt can be made.
subtotals = {"watermelon" : cart["watermelon"] * prices["watermelon"],
             "oranges" : cart["orange"] * prices["orange"]}

#subtotals * tax rate
taxamount = (subtotals["watermelon"] + subtotals["oranges"]) * taxrate

#subtotals + tax amount
total = subtotals["watermelon"] + subtotals["oranges"] + taxamount

#Prints the reciept for Steve.
print(
    "Thanks for shopping at Walmart, Steve!\n" +
    f"Watermelons : ${subtotals['watermelon']:.2f}\n" +
    f"Oranges : ${subtotals['oranges']:.2f}\n" +
    f"Tax : ${taxamount:.2f}\n"+
    f"Total : ${total:.2f}\n" +
    "Payment Method: Cash\n"
    )