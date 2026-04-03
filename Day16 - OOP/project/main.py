from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

maker = CoffeeMaker()
machine = MoneyMachine()

while True:

    choice = input("what would you like? (espresso/latte/cappuccino): ")

    if choice == 'off':
       print("thank you!")
       break
    elif choice == 'report':
        print("current resource: ")
        maker.report()
        machine.report()
    else:
        menus = Menu().find_drink(choice)
        if(menus == None):
            continue

        if(maker.is_resource_sufficient(menus) == False):
            continue
        
        if(machine.make_payment(menus.cost)):
            maker.make_coffee(menus)
            
    