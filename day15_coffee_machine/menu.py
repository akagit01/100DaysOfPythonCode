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

#TODO: 1.Print report of all coffee machine resources

"""
if usr_choice=='r':

    es_ing_water=(MENU["espresso"]["ingredients"]["water"])
    es_ing_coffee=(MENU["espresso"]["ingredients"]["coffee"])
    la_ing_water = (MENU["latte"]["ingredients"]["water"])
    la_ing_coffee = (MENU["latte"]["ingredients"]["coffee"])
    la_ing_milk = (MENU["latte"]["ingredients"]["milk"])
    ca_ing_coffee = (MENU["cappucino"]["ingredients"]["coffee"])
    ca_ing_water = (MENU["cappucino"]["ingredients"]["water"])
    ca_ing_milk = (MENU["cappucino"]["ingredients"]["milk"])
    water=es_ing_water+la_ing_water + ca_ing_water
    coffee=es_ing_coffee + la_ing_coffee + ca_ing_coffee
    milk=la_ing_milk + ca_ing_milk
    print(f"water: {water}ml")
    print(f"coffee: {coffee}g")
    print(f"milk: {milk}ml")

"""


def print_report():
    total_ingredient={}
    for drink in MENU.values():
        #print(drink)
        for ingredient,amount in drink["ingredients"].items():
            #print(ingredient,amount)
            if ingredient in total_ingredient:
                total_ingredient[ingredient]+=amount
            else:
                total_ingredient[ingredient]=amount

    #print(total_ingredient)

    for item,total in total_ingredient.items():
        unit="ml" if item in ["milk","water"] else "g"
        print(f"{item}:{total}")

    return total_ingredient


#TODO: 5. Make Coffee
def make_coffee(usr_choice):

    if usr_choice=='e':
        print("here is your espresso")

    elif usr_choice=='l':
        print("here is your latte")
    elif usr_choice=='c':
        print("here is your cappuccino")



#TODO: 0. Prompt user by asking “What would you like? (espresso/latte/cappuccino)

def order():
    usr_choice=input("what would you like to have? Choose one of the following: \n e for espresso "
                 "\n l for latte \n c for cappuccino \n r for report. \n Enter:")

    if usr_choice=='r':
        print_report()
    if usr_choice in ['e','l','c']:
        make_coffee()
    return usr_choice


#TODO: 2.Check resources sufficient to make drink order.
tot_ing=print_report()
usr_choice=''
updated_water_qty=0
updated_coffee_qty=0
updated_milk_qty=0
for item,amt in tot_ing.items():
    if item=="water":
        updated_water_qty=updated_water_qty+amt
    elif item=="milk":
        updated_milk_qty = updated_milk_qty + amt
    elif item == "coffee":
        updated_coffee_qty = updated_coffee_qty + amt
print(f"updated values of coffee: {updated_coffee_qty},\nupdated values of water: {updated_water_qty},\nupdated values of milk: {updated_milk_qty}, ")

if usr_choice == 'e':
    if updated_coffee_qty>=18 and updated_water_qty>=50:
        updated_water_qty=updated_water_qty-50
        updated_coffee_qty=updated_coffee_qty-18
        make_coffee(usr_choice)
    else:
        print("Not enough ingredients")
elif usr_choice == 'l':
    if updated_coffee_qty>=24 and updated_water_qty>=200 and updated_milk_qty>=150:
        updated_water_qty = updated_water_qty - 200
        updated_coffee_qty = updated_coffee_qty - 24
        updated_milk_qty=updated_milk_qty-150
        make_coffee(usr_choice)
    else:
        print("Not enough ingredients")
elif usr_choice == 'c':
    if updated_coffee_qty>=24 and updated_water_qty>=250 and updated_milk_qty>=100:
        updated_water_qty = updated_water_qty - 250
        updated_coffee_qty = updated_coffee_qty - 24
        updated_milk_qty = updated_milk_qty - 100
        make_coffee(usr_choice)

    else:
        print("Not enough ingredients")
#or usr_choice=='l' or usr_choice=='c':


#TODO: 3. Process coins


#TODO: 4. Check transaction successful



