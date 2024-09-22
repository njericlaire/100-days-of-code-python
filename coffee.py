MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "Money":0
}
def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def trans(res,chos):
    for key in chos:
        res[key]-=chos[key]


def calc_total(pen,nick,dime,quater):
    tt= quater*0.25+dime*0.10+nick*0.05+pen*0.01
    return tt

def transaction(tt,cost,res):
    
    if tt<cost:
        print("Sorry that's not enough money. Money refunded")
    elif tt==cost:
        res["Money"]+=cost
    else:
        res["Money"]+=cost
        change=tt-cost
        print(f"“Here is ${change} dollars in change")

make_coffee=True
while make_coffee:
    
   
    order=input("What would you like? (espresso/latte/cappuccino):")

    if order=="off":
        exit()
    elif order=="report":
        for key in resources:
            print(f"{key}: {resources[key]}")
    else:
        choice=MENU[order]["ingredients"]
        cost=MENU[order]["cost"]
        
        if is_resource_sufficient(choice):
            
            pennies =int(input("Enter the number of pennies "))
            nickles =int(input("Enter the number of nickles "))
            dimes =int(input("Enter the number of dimes "))
            quarters =int(input("Enter the number of quarters "))
        total=calc_total(pennies,nickles,dimes,quarters)
        transaction(total,cost,resources)
        trans(resources,choice)
