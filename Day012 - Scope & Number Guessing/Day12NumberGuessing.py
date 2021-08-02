#Number Guessing Game Objectives:
import random
# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
lives = 1

def game(lives):
    num = random.randint(1,100)
    print(f"The number is {num}")
    while lives > 0:
        guess = int(input("Please enter a whole number guess: "))
        if guess == num:
            print(f"Congrats, you won! The number was {num}")
            return
        elif guess < num:
            lives -= 1
            print(f"Too low! You have {lives} guesses left.")
        else:
            lives -= 1
            print(f"Too high! You have {lives} guesses left.")
    print(f"Game over! The correct number was {num}")
    return

dif = input("Welcome to the number guessing game, type 'e' for easy mode, type 'h' for hard mode: ")
if dif == "e":
    lives = 10
else:
    lives = 5
game(lives)

