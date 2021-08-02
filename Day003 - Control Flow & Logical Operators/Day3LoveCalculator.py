name1 = input("Please enter the first name: ")
name2 = input("Please enter the second name: ")
cName = name1.lower() + name2.lower()

t_count = 0
l_count = 0

t_count = t_count + cName.count("t") + cName.count("r") + cName.count("u") + cName.count("e")
l_count = l_count + cName.count("l") + cName.count("o") + cName.count("v") + cName.count("e")

total = int(str(t_count) + str(l_count))
if(total > 90 or total < 10):
    print(f"Your score is {total}, you go together like coke and mentos.")
elif(total >=40 and total <= 50):
    print(f"Your score is {total}, you are alright together.")
else:
    print(f"Your score is {total}")

