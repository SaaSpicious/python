import information

resources=information.resources
resources["money"]=0


def print_report(resources):
    print(f"Water: {resources["water"]}ml")
    print(f"Milk: {resources["milk"]}ml")
    print(f"Coffee: {resources["coffee"]}g")
    print(f"Money: {resources["money"]}$")


def print_items(dict):
    output = ""
    for n in dict:
        output += n
        output += "/"
    return output


def prompt_coins(coins):
    credit = 0
    for coin in coins:
        amount = int(input(f"How many {coin} do you want to add? "))
        credit += amount * coins[coin]
    credit = float(credit/100)

    return credit


def check_credit(cost,credit):
    return credit >= cost


def check_resources(recipe,resources):
    for n in recipe:
        if resources[n] < recipe[n]:
            print(f"Sorry, not enough {n}.")
            return False
    return True


def process_order(recipe,resources):
    for n in recipe["ingredients"]:
        resources[n] -= recipe["ingredients"][n]
    resources["money"] -= recipe["cost"]
    return resources


selection = ""
while selection != "off":
    print(f"You may select between ({print_items(information.MENU)}report/off)")
    selection = input("What do you want? ")
    if selection == "report":
        print_report(resources)
    elif selection == "off":
        print("Thank you for using the coffee machine!")
    elif selection not in information.MENU:
        print("Invalid selection, please try again!")
    else:
        if check_resources(information.MENU[selection]["ingredients"],resources):
            while not check_credit(information.MENU[selection]["cost"],resources["money"]):
                print("Insufficient credits, please insert coins.")
                resources["money"]+=prompt_coins(information.coins)
                print(f"You have added a total credit of {resources["money"]}$")
            resources=process_order(information.MENU[selection],resources)
            print(f"Here is your {selection}.")


