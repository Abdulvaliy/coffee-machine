from data import MENU
from data import resources

water = resources["water"]
milk = resources["milk"]
coffee = resources['coffee']
money = 0

turn_of_machine = False

while not turn_of_machine:
    choice = input("What would you like? (espresso/latte/cappuccino/report/off): ").lower()
    if choice == "report":
        print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${money}")
    elif choice == 'off':
        print("Have a good time!")
        turn_of_machine = True
    elif choice != 'espresso' and choice != 'latte' and choice != 'cappuccino':
        print("Wrong input")
        turn_of_machine = True
    else:
        price = MENU[choice]['cost']
        WATER = MENU[choice]['ingredients']['water']
        MILK = MENU[choice]['ingredients']['milk']
        COFFEE = MENU[choice]['ingredients']['coffee']
        #print(MILK)

        print("Please, insert coins.")
        quarter = int(input("How many quarters?: ")) * 0.25
        dime = int(input("How many dimes?: ")) * 0.10
        nickle = int(input("How many nickles?: ")) * 0.05
        penny = int(input("How many pennies?: ")) * 0.01
        Sum = round(float(quarter + dime + nickle + penny), 2)

        if water <= 0 or milk <= 0 or coffee <= 0:
            print("Ran out of resources, Sorry!")
            turn_of_machine = True
        elif Sum >= price:
            # if choice == 'espresso':
            #     print(f"Here is ${Sum - price} in change.")
            #     print(f"you selected {choice}, {water}ml water, {milk}ml milk, {coffee}g coffee left")
            #
            # elif choice == 'latte':
            #     print(f"Here is ${Sum - price} in change.")
            #     print(f"you selected {choice}, {water}ml water, {milk}ml milk, {coffee}g coffee left")
            #
            # elif choice == 'cappuccino':
            #     print(f"Here is ${Sum - price} in change.")
            #     print(f"you selected {choice}, {water}ml water, {milk}ml milk, {coffee}g coffee left")
            water -= WATER
            milk -= MILK
            coffee -= COFFEE
            money += price
            print(f"Here is ${Sum - price} in change.")
            print(f"you selected {choice}, {water}ml water, {milk}ml milk, {coffee}g coffee left")

        elif Sum < price:
            print(f"Price of {choice} is ${price}.\nNot enough money!")
            turn_of_machine = True
        print(f'We have ${money} money now')