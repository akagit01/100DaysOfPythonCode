MENU = {
    "espresso": {
        "ingredients": {"water": 50, "coffee": 18},
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {"water": 200, "milk": 150, "coffee": 24},
        "cost": 2.5,
    },
    "cappucino": {
        "ingredients": {"water": 250, "milk": 100, "coffee": 24},
        "cost": 3.0,
    }
}

# Initial resource levels
water_qty = 1000
milk_qty = 800
coffee_qty = 500

def print_report():
    print(f"Water: {water_qty}ml")
    print(f"Milk: {milk_qty}ml")
    print(f"Coffee: {coffee_qty}g")

def ingredient_check(drink):
    global water_qty, milk_qty, coffee_qty
    ingredients = MENU[drink]["ingredients"]
    if ingredients.get("water", 0) > water_qty:
        print("Sorry, not enough water.")
        return False
    if ingredients.get("milk", 0) > milk_qty:
        print("Sorry, not enough milk.")
        return False
    if ingredients.get("coffee", 0) > coffee_qty:
        print("Sorry, not enough coffee.")
        return False
    return True

def deduct_ingredients(drink):
    global water_qty, milk_qty, coffee_qty
    ingredients = MENU[drink]["ingredients"]
    water_qty -= ingredients.get("water", 0)
    milk_qty -= ingredients.get("milk", 0)
    coffee_qty -= ingredients.get("coffee", 0)

def process_coin(drink):
    try:
        qtr = float(input("Quarters: "))
        dimes = float(input("Dimes: "))
        nick = float(input("Nickels: "))
        pennies = float(input("Pennies: "))
    except ValueError:
        print("Invalid input.")
        return False

    total = qtr * 0.25 + dimes * 0.10 + nick * 0.05 + pennies * 0.01
    cost = MENU[drink]["cost"]
    print(f"Total inserted: ${total:.2f}")

    if total < cost:
        print("Sorry, not enough money. Money refunded.")
        return False
    if total > cost:
        print(f"Here is ${round(total - cost, 2)} in change.")
    return True

def make_coffee(choice):
    drinks = {'e': 'espresso', 'l': 'latte', 'c': 'cappucino'}
    if choice not in drinks:
        if choice == 'r':
            print_report()
            return True
        else:
            print("Invalid choice.")
            return True

    drink = drinks[choice]
    if not ingredient_check(drink):
        return False
    if not process_coin(drink):
        return True

    deduct_ingredients(drink)
    print(f"Here is your {drink}. Enjoy! ☕")
    return True

def usr_order():
    return input("What would you like? (e: espresso, l: latte, c: cappuccino, r: report): ").lower()

# Main loop
not_need_maintenance = True
while not_need_maintenance:
    order = usr_order()
    print("\n" * 3)
    not_need_maintenance = make_coffee(order)
    print(f"Machine operational: {not_need_maintenance}")
