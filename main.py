from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

IS_ON = True

coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

while IS_ON:
    # espresso / latte / cappuccino
    choice = input("What would you like?" + " " + menu.get_items() + " ")

    if choice == 'off':
        print("this coffee machine now turn off")
        is_on = False
    elif choice == 'report':
        # print ingredients!.
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if drink:
            if coffee_maker.is_resource_sufficient(drink):
                money_machine.make_payment(drink.cost)
                coffee_maker.make_coffee(drink)
