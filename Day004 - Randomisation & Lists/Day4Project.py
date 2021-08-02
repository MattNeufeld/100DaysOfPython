import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
playing = True
while(playing):
    player = int(input("Please choose '0' for Rock, '1' for Paper, '2' for Scissors, or '3' to stop playing"))
    if(player == 3):
        playing = False
    else:
        rand = random.randint(0,2)
        if (player == 0):
            p_choice = rock
        elif (player == 1):
            p_choice = paper
        else:
            p_choice = scissors
            
        print(f"Player: {p_choice}")

        if(rand == 0):
            computer = rock
            print(f"Computer: {computer}")
            if (player == 0):
                print("Game was a tie")
            elif (player == 1):
                print("You Win!")
            else:
                print("You Lose!")
        elif(rand == 1):
            computer = paper
            print(f"Computer: {computer}")
            if (player == 0):
                print("You Lose!")
            elif (player == 1):
                print("Game was a tie")
            else:
                print("You Win!")
        else:
            computer = scissors
            print(f"Computer: {computer}")
            if (player == 0):
                print("You Win!")
            elif (player == 1):
                print("You Lose!")
            else:
                print("Game was a tie")
print("Thank you for playing!")
