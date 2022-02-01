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
}
# ---------- (End of given code) ----------

monies = 0
from art import logo

print(logo)


def check_resources(drinkchosen):
    """Checks each ingredient in the machine to make sure enough is provided for selected drink"""
    for ingredient in drinkchosen:
        if drinkchosen[ingredient] > resources[ingredient]:
            print(f"Sorry, not enough {ingredient}.")
            return False
    return True


def remove_resources(drinkordered):
    """Removes a successful order's ingredients from the resources"""
    for ingredient in drinkordered:
        resources[ingredient] -= drinkordered[ingredient]


coffee_time = True
while coffee_time:

    # TODO 1. Prompt user by asking “ What would you like? (espresso/latte/cappuccino): ”

    choice_drink = input("What would you like? (espresso - $1.50/latte - $2.50/cappuccino - $3.00): ").lower()

    # TODO 2. Turn off the Coffee Machine by entering “ off ” to the prompt.

    if choice_drink == "off":
        coffee_time = False

    # TODO 3. Print report

    elif choice_drink == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${monies}")

    # TODO 4. Check resources sufficient

    else:
        our_drink = MENU[choice_drink]
        if check_resources(our_drink["ingredients"]):
            # TODO 5. Process coins

            print("Please insert coins now.")
            coins_q = int(input("How many quarters?: "))
            coins_q = round(coins_q * 0.25, 2)
            print(f"${coins_q} has been inserted.")

            coins_d = int(input("How many dimes?: "))
            coins_d = round(coins_d * 0.10, 2)
            print(f"${coins_q + coins_d} has been inserted.")

            coins_n = int(input("How many nickels?: "))
            coins_n = round(coins_n * 0.05, 2)
            print(f"${round(coins_q + coins_d + coins_n, 2)} has been inserted.")

            coins_p = int(input("How many pennies?: "))
            coins_p = round(coins_p * 0.01, 2)

            coins_total = round(coins_q + coins_d + coins_n + coins_p, 2)
            print(f"You have inserted ${coins_total} into the machine.")

            # TODO 6. Check transaction successful?

            if coins_total < our_drink['cost']:
                print(f"Sorry, that's not enough money for a {choice_drink}. Refunding money... ")
            elif coins_total >= our_drink['cost']:
                refund = coins_total - our_drink['cost']
                print(f"Here is your ${refund} in change.")
                print(f"Enjoy your {choice_drink}!")

                # TODO 7. Make coffee

                remove_resources(our_drink['ingredients'])
                monies += our_drink['cost']
