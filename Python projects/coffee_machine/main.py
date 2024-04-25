from money_machine import MoneyMachine
from coffee_maker import CoffeeMaker
from menu import Menu, MenuItem

def TakeOrder():
    m = Menu()
    cm = CoffeeMaker()
    mm  =MoneyMachine()
    cost = 0
    print("\n\nHey there!, ",end ='')
    while True:
        order = input(f"what would you like to have {m.get_items()}?").lower()
        #PRINTING RESOURCES AVAILABLE
        if order == "report":
            print("Resources available are : ")
            cm.report()
        #EXITING
        elif order == "exit":
            print("Thank you for visiting!")
            return 
        #ORDERING A DRINK
        else:
            drink = m.find_drink(order)
            if drink:
                print(f'''
Ingredients of  {order} are : 
{drink.ingredients}''' )
                if cm.is_resource_sufficient(drink):
                    
                    choice = input("Do you to confirm you order? :").lower()
                    if choice[0] == 'y':
                        cost += drink.cost
                        cm.make_coffee(drink)
                        print(f"Great!, your bill is ${cost}")
                        mm.make_payment(cost)
                    else:
                        print("Ok, then!")
                else:
                    print("Not enough resources are available to make the drink")
                    cm.report()
                     
TakeOrder()  

                