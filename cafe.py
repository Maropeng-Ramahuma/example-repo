
#List of things sold in the cafe
menu = ["muffin", "sandwich", "buns", "coffee", "hot chocholate", "ice tea"]

#Dictionary with the amount of stock we have 
inventory = {
             "muffin": 30,
             "sandwich": 15,
             "buns" : 20,
             "coffee" : 35,
             "hot chocholate": 5,
             "ice tea" : 10}

#create a dictionary that gives price to each
cost_price = {
            "muffin": 15,
             "sandwich": 35,
             "buns" : 10,
             "coffee" : 26,
             "hot chocholate": 30,
             "ice tea" : 40}

#variable for the how much the stock costs
total_inventory = 0

#use for loop to calculate the item price for each
for item in menu:
    item_price = inventory[item] * cost_price[item]
    total_inventory += item_price

print("Total inventory cost value is: R", total_inventory)