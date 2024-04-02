import os

def auction():
  
  bid = {}
  while True:
    print("Welcome to the auction!")
    name = input("What is your name? ")
    bid_amount = int(input("What is your bid? $"))
    bid[name] = bid_amount
    bidder = input("Are there any other bidders? Type 'yes' or 'no'. ")
    if bidder == "no":
      break
    os.system('cls')
  highest_bid = 0
  bidder_name= ''
  for bidder in bid:
    if bid[bidder] > highest_bid:
      highest_bid = bid[bidder]
      bidder_name = bidder

  print(f"Congratulations {bidder_name}! You won the auction for ${highest_bid}")

auction()