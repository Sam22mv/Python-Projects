from random import choice

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.50,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "coffee": 24,
            "milk": 150,
        },
        "cost": 2.50,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "coffee": 24,
            "milk": 100,
        },
        "cost": 3.00,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

def sum_coin(quaters,dimes,nickles,pennis):
    q = 0.25 * quaters
    d = 0.10 * dimes
    n = 0.05 * nickles
    p = 0.01 * pennis

    sum = q + d + n + p
    return sum

def espresso(quaters,dimes,nickles,pennis):
    cost = 1.50
    esp = sum_coin(quaters, dimes, nickles, pennis) - cost
    if esp < 0:
        return "insufficient money"
    else:
        global profit
        profit += cost
        return f"here is your espresso and change {esp} and profit {profit}"

def latte(quaters,dimes,nickles,pennis):
    cost = 2.50
    lat = sum_coin(quaters, dimes, nickles, pennis) - cost
    if lat < 0:
        return "insufficient money"
    else:
        global profit
        profit += cost
        return f"here is your latte and change {lat} and profit {profit}"

def cappuccino(quaters,dimes,nickles,pennis):
    cost = 3.00
    cap = sum_coin(quaters, dimes, nickles, pennis) - cost
    if cap < 0:
        return "insufficient money"
    else:
        global profit
        profit += cost
        return f"here is your cappuccino and change {cap} and profit {profit}"


def is_resources_sufficient(order_ingredients):
    enough = True
    for value in order_ingredients:
        if order_ingredients[value] >= resources[value]:
            print(f"sorry there is not enought {value}")
            enough = False
    return enough

def make_coffe(drink_name, order_ingredients):
    for value in order_ingredients:
        resources[value] -= order_ingredients[value]
    print(f"here is your {drink_name}")

profit = 0
coffee = True
while coffee:

    user = input("what wold you like? (espresso/latte/cappuccino): ").lower()

    if user == 'off':
        coffee = False

    elif user == 'report':
        for key, value in resources.items():
            print(f"{key}: {value}")
        print(f"money: ${profit}")

    else:
        drink = MENU[user]
        if is_resources_sufficient(drink["ingredients"]):

            if user == 'espresso' or user == 'latte' or user == 'cappuccino':
                print("please insert coins.")
                quaters = int(input("how many quaters?: "))
                dimes = int(input("how many dime?: "))
                nickles = int(input("how many nickles?: "))
                pennis = int(input("how many pennis?: "))
            if user == 'espresso':
                print(espresso(quaters,dimes,nickles,pennis))
                make_coffe()
            elif user == 'latte':
                print(latte(quaters,dimes,nickles,pennis))
                make_coffe(user, drink["ingredients"])
            elif user == 'cappuccino':
                print(cappuccino(quaters,dimes,nickles,pennis))
                make_coffe()







