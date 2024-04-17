import random

# Sample menu
menu = {
    "Margherita": 10.99,
    "Pepperoni": 12.99,
    "Vegetarian": 11.99,
    "Hawaiian": 13.99,
    "Meat Lover's": 14.99
}

crust = {
    "regular":0.00,
    "thin" : 1.00, 
    "pan" : 3.00,
    "cheeseburst": 5.00
}

# Function to greet the user
def greet():
    return "Hello! Welcome to our pizza delivery service. How can I assist you today?"

# Function to display the menu
def display_menu():
    menu_list = "\n".join([f"{item}: ${price}" for item, price in menu.items()])
    print(f"Here's our menu:\n{menu_list}") 

def confirm_order(order,cost):
    print(f'Your current order is : {order}')
    print(f'Total cost is {cost}')
    choice  = int(input('''Would you like to confirm your order : 
          1-yes
          2-no\n'''))
    
    return choice
    
    

# Function to place an order
def place_order():
    order = []
   
    cost = 0
    while(True):
        pizza = input("What pizza would you like to have? ")
        
        if pizza in menu:
            cost += menu[pizza]
            size = input("Great choice! Next, please select the size S/M/L : ").lower()
            if size == 'm':
                cost += 0.3*cost
            elif size == 'l':
                cost += 0.5*cost
            print(f"Cost so far : {cost}")
            print("What type of crust would you like?")
            print(crust)
            type = input(">")
            cost += crust[type]
            order.append({"pizza":pizza, "crust":type, "cost": cost})
            choice = input("Would you like to order another pizza?").lower()
            if choice == 'n' or choice =='no':
                c = confirm_order(order,cost)
                if c==1:
                    print(f"Your order has been placed!, Your bill is : {cost + 0.18*menu[pizza]} G.S.T included")
                    print("Thank you for visiting us,have a nice day!")
                    return 
                if c==2:
                    order.clear()
            
            
        else:
            print("Kindly provide a valid pizza name")
            display_menu()
        

        


# Main function to run the chatbot
def run_chatbot():
    print(greet())
    display_menu()
    place_order()

# Run the chatbot
if __name__ == "__main__":
    run_chatbot()
