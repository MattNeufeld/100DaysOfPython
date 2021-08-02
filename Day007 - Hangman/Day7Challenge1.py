import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)

guess = (input("Guess a single letter in the word: ")).lower()

if(guess in chosen_word):
    print(f"{guess} is in the word!")
else:
    print("Incorrect guess")

