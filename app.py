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
    },

    {
        "item": "Essentials Hoodie",
        "price": 90,
        "size": "M",
        "description": "Gray Essentials hoodie"
    },

    {
        "item": "Uniqlo Jeans",
        "price": 60,
        "size": "28/30",
        "description": "Light Blue Barrel-Baggy Jeans"
    },

    {
        "item": "Denim Tears Hoodie",
        "price": 210,
        "size": "M",
        "description": "Gray and White 'The Cotton Wreath' hoodie"
    },
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
        print(f"[{i}] Name: {clothingStore[i]["item"]} \n Price: ${clothingStore[i]["price"]} \n Size: {clothingStore[i]["size"]} \n'{clothingStore[i]["description"]}' \n")

wantToBuy = True

while wantToBuy:
    showItemList()
    
    userPurchase = int(input("Which item would you like to purchase?: "))
    cart.append(clothingStore[userPurchase])
    
    confirm = input("Do you still want to continue browsing? y/n ")
    if confirm == "n":
        break
    else:
        wantToBuy=True

print("\nCart Items: ")

total = 0
for i in range(len(cart)):
    print(f"    {cart[i]["item"]} - ${cart[i]["price"]}")
    total += cart[i]["price"]


print(f"\nTotal: ${total}")
