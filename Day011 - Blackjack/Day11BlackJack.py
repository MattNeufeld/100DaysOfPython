import random
end = False
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

def deal():
    num = random.choice(cards)
    return num

def calc_score(hand):
    total = 0
    for i in hand:
        total = total + i
        if 11 in hand and total > 21:
            total = total - 10
    return total
    

def game():
    user = []
    comp = []
    choice = "y"
    for i in range(2):
        user.append(deal())
        comp.append(deal())
    print(f"Your hand is: {user}")
    print(f"Dealer's first card: {comp[0]}")
    if calc_score(user) == 21:
        print("BLACKJACK! You win!")
        print("\n\n\n\n\n\n\n")
        return
    while choice != "n":
        choice = input("Type 'y' to get another card, type 'n' to pass: ")
        if choice == "y":
            user.append(deal())
            print(f"Your hand is: {user}")
            if calc_score(user) > 21:
                print("You went over 21, you lose")
                print("\n\n\n\n\n\n\n")
                return
    while calc_score(comp) < 17:
        comp.append(deal())
    print(f"Your final hand is: {user}")
    print(f"Dealer's final hand is: {comp}")
    user_s = calc_score(user)
    comp_s = calc_score(comp)
    if comp_s > 21:
        print(f"The dealer went over, you win!")
    elif user_s > comp_s:
        print(f"You win!")
    elif user_s == comp_s:
        print("Draw!")
    else:
        print("You lose!")
    print("\n\n\n\n\n\n\n")
        

while not end:
    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if play == "y":
        game()
    else:
        end = True
        print("Thanks for playing")
