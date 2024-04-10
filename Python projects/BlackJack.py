import random 

cards  = {}

for i in range(2,12):
    cards[i]=4
# print(cards)
    
def play_game():
    user_cards, comp_cards=[],[]
    user_sum, comp_sum = 0,0
    for i in range(2):
        card = random.randint(2,11)
        cards[card]-=1
        user_cards.append(card)
    if sum(user_cards)==22:
        user_cards[1]=1
    user_sum = sum(user_cards)
    print(f"Your cards are : {user_cards} and your sum is {user_sum}")

    for i in range(2):
        card = random.randint(2,11)
        cards[card]-=1
        comp_cards.append(card)

    comp_sum= sum(comp_cards)
    print(f"computer's first card is :   {comp_cards[0]}")

    while True:
        choice = input(("what would you like to do h(hit)/s(stand):")).lower()
        if choice =='h':
            
            card = random.randint(2,11)

    return

choice = 'y'
while choice == 'y':
    choice  = input("Would you like to play a game of black jack y/n : ")
    if choice =='y':
        play_game()
    