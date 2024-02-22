import random as rm
import time
import math

name = input("Greetings user, what is your name : ")
print(f"{name}!...., Sounds like a wonderful name")

low, high = map(int,input("Enter range for the game : ").split())
print("Generating random number .....")
obj = rm.Random(time.time())
random_number = obj.randint(low,high)

max_guesses = int(math.log(high-low+1,2))
for i in range(max_guesses):
    guess = int(input("Your guess : "))
    if guess == random_number:
        print(f"Hurray, you guessed it right! Number of tries required : {i+1}")
        break
    else:
        if i==max_guesses-1:
            print("Incorrect, better luck next time!")
            print(f"The correct answer : {random_number}")
        else:
            print(f"Nope, you have {max_guesses-i-1} chances left")
    
    