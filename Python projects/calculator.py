import os

calc = '''
|  _________________  |
| |              0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|'''

def calculator():
    print(calc)
    '''Does arithmetic operations on the provided input
    Type exit to exit the program.'''

    dec = "y"
    while dec == "y" or dec == "yr":

        if dec == "yr":
            a = result
        else:
            a = float(input("Enter your first operand : "))
        o = input("Enter your operator : ")
        b = float(input("Enter your second operand : "))
        
        def add(a,b):
            return a+b
        def subtract(a,b):
            return a-b
        def multiply(a,b):
            return a*b
        def divide(a,b):
            return a/b
        
        operators = {'*':multiply, '+': add, '-':subtract, '/':divide}
        result = (operators[o])(a,b)
        if result//1 ==result:
            result  = int(result)
        print(result)

        dec = input("Continue(y)/Continue with same result(yr)/Exit(exit) : ")
        if dec == "y":
            os.system('cls')
        if dec =="exit":
            print("Exiting...")
            return 

calculator()
# print hello world
