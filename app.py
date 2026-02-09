clothingStore = [
    {
        "item": {
            "name": "Blank Sweatpants",
            "price": 40,
            "size": "M",
            "description": "Gray sweatpants",
        }
    },

    {
        "item1": {
            "name":"Blank hoodie",
            "price": 55,
            "size": "L",
            "description": "Black hoodie"
        }
    }, 

    {
        "item2": { 
            "name":"Designer hoodie",
            "price": 800,
            "size": "L",
            "description": "Chrome Hearts hoodie"
        }
    },
]

# Part One

order = input("Which one item do you want to purchase? (0-2): ")
print(clothingStore[clothingStore.index(order)]["item"])

