clothingStore = [
    {
        "item": "Blank Sweatpants",
        "price": 40,
        "size": "M",
        "description": "Gray sweatpants",
    },

    {
        "item": "Blank Hoodie",
        "price": 55,
        "size": "L",
        "description": "Black hoodie"
    }, 

    {
        "item": "Designer Hoodie",
        "price": 800,
        "size": "L",
        "description": "Chrome Hearts hoodie"
    }
]


# Part One
"""
order = input("Which one item do you want to purchase? (0-2): ")
print(clothingStore[int(order)]["item"])
"""

# Part Two

cart = []
def showItemList():
    print("Browse: ")
    for i in range(len(clothingStore)):
        print(f"Name: {clothingStore[i]["item"]} \n Price: {clothingStore[i]["price"]} \n Size: {clothingStore[i]["size"]} \n'{clothingStore[i]["description"]}' \n")

wantToBuy = True

while wantToBuy:
    showItemList()
    userPurchase = input("Which item would you like to purchase?: ")
    cart.append(clothingStore[f"{userPurchase}"])
    
    confirm = input("Do you still want to continue browsing? y/n")
    if confirm == "n":
        break
#userinput change to numerical***