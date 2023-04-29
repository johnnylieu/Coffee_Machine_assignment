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


# TODO 1. Prompt user by asking "What would you like? (expresso/latte/cappuccino):"
#  1a: Check the user’s input to decide what to do next.
#  1b: The prompt should show every time action has completed, e.g. once the drink is dispensed.
#  The prompt should show again to serve the next customer.

# TODO 2. Turn off the Coffee Machine by entering “off” to the prompt.
#  2a: For maintainers of the coffee machine, they can use “off” as the secret word to turn off the machine.
#  Your code should end execution when this happens
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


# TODO 3. Print report
#  3a. When the user enters “report” to the prompt, a report should be generated that shows
#  the current resource values. e.g.
#  Water: 100ml
#  Milk: 50ml
#  Coffee: 76g
#  Money: $2.5
def print_report():
    """prints available resources"""
    r = resources
    print(f'Water: {r["water"]}ml\nMilk: {r["milk"]}ml\nCoffee: {r["coffee"]}g\nMoney: ${r["money"]}\n')
    prompt()


# TODO 4. Check resources sufficient?
#  4a: When the user chooses a drink, the program should check if there are enough
#  resources to make that drink.
#  4b: E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should
#  not continue to make the drink but print: “Sorry there is not enough water.”
#  4c: The same should happen if another resource is depleted, e.g. milk or coffee.
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


# TODO 5: Process coins
#  5a: If there are sufficient resources to make the drink selected,
#  then the program should prompt the user to insert coins.
#  5b: Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
#  5c: Calculate the monetary value of the coins inserted.
#   E.g. 1 quarter, 2 dimes, 1 nickel, 2 pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52
#   round to two decimals
def insert_coins(drink, water_amount, milk_amount, coffee_amount, water, milk, coffee):
    """returns the total amount that user paid"""
    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.1
    nickels = int(input("How many nickels?: ")) * 0.05
    pennies = int(input("How many pennies?: ")) * 0.01

    all_coins = (quarters, dimes, nickels, pennies)

    total = round(sum(all_coins), 2)

    check_transaction(total, drink, water_amount, milk_amount, coffee_amount, water, milk, coffee)


# TODO 6: Check transaction successful?
#  6a: Check that the user has inserted enough money to purchase the drink they selected.
#   E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
#   program should say “Sorry that's not enough money. Money refunded.”.
#  6b: But if the user has inserted enough money, then the cost of the drink gets added to the
#   machine as the profit and this will be reflected the next time “report” is triggered. E.g.
#       Water: 100ml
#       Milk: 50ml
#       Coffee: 76g
#       Money: $2.5
#  6c: If the user has inserted too much money, the machine should offer change.
#   E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal places.
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


# TODO 7: Make coffee
#  7a: If the transaction is successful and there are enough resources to make the drink the
#   user selected, then the ingredients to make the drink should be deducted from the
#   coffee machine resources.
#   E.g. report before purchasing latte:
#       Water: 300ml
#       Milk: 200ml
#       Coffee: 100g
#       Money: $0
#   Report after purchasing latte:
#       Water: 100ml
#       Milk: 50ml
#       Coffee: 76g
#       Money: $2.5
#   7b: Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”.
#       If latte was their choice of drink.
def make_coffee(water_amount, milk_amount, coffee_amount, water, milk, coffee):
    """if transaction is successful and there are enough resources, make coffee"""
    money = resources["money"]
    water_amount -= water
    milk_amount -= milk
    coffee_amount -= coffee
    print(f"Resources:\nWater: {water_amount}ml\nMilk: {milk_amount}ml\nCoffee: {coffee_amount}g\nMoney: ${money}\n")


if __name__ == "__main__":
    prompt()
