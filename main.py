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
    "money": 0
}


def prompt():
    """prompts the user for which drink they would like. 'off' turns off coffee machine"""
    prompt_response = input(f"What would you like? (expresso/latte/cappuccino): ").lower()

    if prompt_response == "off":
        quit()
    elif prompt_response == "report":
        return print_report()
    elif prompt_response in {"expresso", "latte", "cappuccino"}:
        return check_resources(prompt_response)
    else:
        print("Incorrect choice!\n")
        return prompt()


def print_report():
    """prints available resources"""
    r = resources
    print(f'Water: {r["water"]}ml\nMilk: {r["milk"]}ml\nCoffee: {r["coffee"]}g\nMoney: ${r["money"]}\n')
    prompt()


def check_resources(drink):
    """checks if we have enough resources"""

    water_amount = resources["water"]
    milk_amount = resources["milk"]
    coffee_amount = resources["coffee"]

    water = MENU[drink]["ingredients"]["water"]
    milk = MENU[drink]["ingredients"]["milk"]
    coffee = MENU[drink]["ingredients"]["coffee"]

    if (water_amount >= water) and (milk_amount >= milk) and (coffee_amount >= coffee):
        insert_coins(drink, water_amount, milk_amount, coffee_amount, water, milk, coffee)
    elif water_amount < water:
        print('Sorry there is not enough water')
    elif milk_amount < milk:
        print('Sorry there is not enough milk')
    elif coffee_amount < coffee:
        print('Sorry there is not enough coffee')
    prompt()


def insert_coins(drink, water_amount, milk_amount, coffee_amount, water, milk, coffee):
    """returns the total amount that user paid"""
    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.1
    nickels = int(input("How many nickels?: ")) * 0.05
    pennies = int(input("How many pennies?: ")) * 0.01

    all_coins = (quarters, dimes, nickels, pennies)

    total = round(sum(all_coins), 2)

    check_transaction(total, drink, water_amount, milk_amount, coffee_amount, water, milk, coffee)


def check_transaction(total, drink, water_amount, milk_amount, coffee_amount, water, milk, coffee):
    """checks if transaction is successful"""
    cost = MENU[drink]["cost"]
    user_money = total
    resources["money"] += total
    change = round((user_money - cost), 2)

    if user_money < cost:
        print(f'Sorry ${user_money} is not enough money, one {drink} is ${cost}. Money refunded.\n')
        prompt()
    elif user_money >= cost:
        print(f"\nHere is ${change} in change. Enjoy your {drink}!\n")
        resources["money"] -= change
        resources["money"] = round((resources["money"]), 2)
        make_coffee(water_amount, milk_amount, coffee_amount, water, milk, coffee)


def make_coffee(water_amount, milk_amount, coffee_amount, water, milk, coffee):
    """if transaction is successful and there are enough resources, make coffee"""
    money = resources["money"]
    water_amount -= water
    milk_amount -= milk
    coffee_amount -= coffee
    print(f"Resources:\nWater: {water_amount}ml\nMilk: {milk_amount}ml\nCoffee: {coffee_amount}g\nMoney: ${money}\n")


if __name__ == "__main__":
    prompt()
