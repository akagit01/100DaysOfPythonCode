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
    # print(drink)
    for ingredient, amount in drink["ingredients"].items():
        # print(ingredient,amount)
        if ingredient in total_ingredient:
            total_ingredient[ingredient] += amount
        else:
            total_ingredient[ingredient] = amount

     #print(total_ingredient)
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

es_cost=MENU["espresso"]["cost"]
la_cost=MENU["latte"]["cost"]
ca_cost=MENU["cappucino"]["cost"]
print(f"cost of espresso: {es_cost}, cost of latte: {la_cost}, cost of cappucino: {ca_cost}")


def switch_off():
    print("turning off")
    return exit
def ingredient_check(order):
    global water_qty,coffee_qty,milk_qty

    if water_qty<50 or coffee_qty<18 or milk_qty<100:
        switch_off()

    elif order=='e':
        water_qty -= 50
        coffee_qty = coffee_qty - 18

    elif order=='l':
        water_qty = water_qty - 200
        coffee_qty = coffee_qty - 24
        milk_qty = milk_qty - 150
    elif order=='c':
        water_qty = water_qty - 250
        coffee_qty = coffee_qty - 24
        milk_qty = milk_qty - 100


    return water_qty,coffee_qty,milk_qty

def process_coin(order):
    qtr = float(input("Please place a value against how many coins in that denomination would you like to insert\n"
                "quarters: "))
    dimes = float(input("Please place a value against how many coins in that denomination would you like to insert\n"
                  "dimes: "))
    nick = float(input("Please place a value against how many coins in that denomination would you like to insert\n"
                 "nickles: "))
    pennies = float(input("Please place a value against how many coins in that denomination would you like to insert\n"
                    "pennies: "))
    coin_denomination={"qtr":0.25,"dimes":0.10,"nick":0.05,"pennies":0.01,}
    total_amt=qtr*coin_denomination["qtr"]+dimes*coin_denomination["dimes"]+nick*coin_denomination["nick"]+pennies*coin_denomination["pennies"]
    print(f"amount inserted: {total_amt}")
    if order=='e':
        if total_amt==1.5:
            return True
        elif total_amt<1.5:
            print("sorry not enough coins")
    elif order=='l':
        if total_amt==2.5:
            return True
        elif total_amt<2.5:
            print("sorry not enough coins")
    elif order=='c':
        if total_amt==3.0:
            #make_coffee(order)
            return True
        elif total_amt<3.0:
            print("sorry not enough coins")




def print_report():
    global water_qty,milk_qty,coffee_qty
    print(f"water: {water_qty} \ncoffee: {coffee_qty} \n milke_qty: {milk_qty}")

def make_coffee(usr_choice):

    if usr_choice=='e':
        print("here is your espresso")
        w,m,c=ingredient_check(usr_choice)
        print(f"machine is left with \nwater= {w}\nmilk={m}\ncoffee={c}")

    elif usr_choice=='l':
        print("here is your latte")
        w, m, c = ingredient_check(usr_choice)
        print(f"machine is left with \nwater= {w}\nmilk={m}\ncoffee={c}")
    elif usr_choice=='c':
        print("here is your cappuccino")
        w, m, c = ingredient_check(usr_choice)
        print(f"machine is left with \nwater= {w}\nmilk={m}\ncoffee={c}")
    elif usr_choice=='r':
        print_report()


def usr_order():
    usr_choice=input("what would you like to have? Choose one of the following: \n e for espresso "
                 "\n l for latte \n c for cappuccino \n r for report. \n Enter:")

    if usr_choice=='r':
        print_report()
    elif usr_choice in ['e','l','c']:
        enough_coins=process_coin(usr_choice)
        #print(enough_coins)
        if enough_coins:
            make_coffee(usr_choice)
    return usr_choice

maintenance=False

while not maintenance:

    order=usr_order()
    ingredient_check(order)
    maintenance=input()



