#incomplete code
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
money = 0
end = False


def print_report():
    print(f"Water: {resources['water']}")
    print(f"Milk: {resources['milk']}")
    print(f"Coffee: {resources['coffee']}")
    print(f"Money: ${money}")


def get_change(q, d, n, p, cost):
    total = q * 0.25 + d * 0.10 + n * 0.05 + p * 0.01
    if (total - cost < 0):
        print("Not enough coins inserted")
        return False
    else:
        print(f"Here is ${total - cost} in change.")
        return True


while not end:
    req = input("What would you like? (espresso/latte/cappuccino): ")
    req = req.lower()
    if req == "report":
        print_report()
    else:
        drink = MENU[req]
        cost = drink['cost']
        mat = drink["ingredients"]
        reqW = mat["water"]
        reqM = mat["milk"]
        reqC = mat["coffee"]
        if reqW > resources["water"]:
            print("Sorry there is not enough water")
        elif reqM > resources["milk"]:
            print("Sorry there is not enough milk")
        elif reqC > resources["coffee"]:
            print("Sorry there is not enough coffee")
        else:
            quarter = int(input("How many quarters?: "))
            dime = int(input("How many dimes?: "))
            nickel = int(input("How many nickels?: "))
            penny = int(input("How many pennies?: "))
            drink = MENU[req]
            paid = get_change(quarter, dime, nickel, penny, cost)
            if paid:
                cost = drink['cost']
                money += cost
                resources["water"] = resources["water"] - reqW
                resources["milk"] = resources["milk"] - reqM
                resources["coffee"] = resources["coffee"] - reqC

