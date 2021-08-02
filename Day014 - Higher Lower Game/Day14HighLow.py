import game_data
import random
import art
print(art.logo)
end = False
data_list = game_data.data
score = 0

def answer(a, b):
    if(a['follower_count'] > b['follower_count']):
        return "a"
    elif (a['follower_count'] == b['follower_count']):
        return "same"
    else:
        return "b"

while not end:
    choiceA = random.choice(data_list)
    list2 = data_list
    list2.remove(choiceA)
    choiceB = random.choice(list2)
    #print(choiceA)
    #print(choiceB)
    print(f"Compare A: {choiceA['name']}, a {choiceA['description']}, from {choiceA['country']}")
    print(art.vs)
    print(f"Against B: {choiceB['name']}, a {choiceB['description']}, from {choiceB['country']}")
    more = input("Who has more followers? Type 'A' or 'B': ")
    ans = answer(choiceA, choiceB)
    if(ans == "same" or ans == more.lower()):
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
        end = True

print(f"Your final score was: {score}")
