import maths2
MENU={
    "espresso":{
        "ingredients": {
            "water":50,
            "coffee":18,
        },
        "cost":1.5,
    },
    "latte":{
        "ingredients": {
            "water":200,
            "milk":150,
            "coffee":24,
        },
        "cost":2.5,
    },
    "cappucino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}


water_qty=0
milk_qty=0
coffee_qty=0
for drink in MENU.values():
    total_ingredient = {}
    #print(drink)

    for ingredient, amount in drink["ingredients"].items():
        # print(ingredient,amount)
        if ingredient in total_ingredient:
            total_ingredient[ingredient] += amount
        else:
            total_ingredient[ingredient] = amount

    print(total_ingredient)
    """
    for item, total in total_ingredient.items():
        if item=='water':
            water_qty+=total
        elif item=='milk':
            milk_qty+=total
        elif item=='coffee':
            coffee_qty+=total
    #unit = "ml" if item in ["milk", "water"] else "g"
    #print(f"{item}:{total}")
print(f"water: {water_qty},milk: {milk_qty}, coffee: {coffee_qty}")
    """