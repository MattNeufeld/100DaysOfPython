print("Welcome to the tip calculator.")
total = float(input("What was the total bill? $"))
percent = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
split = int(input("How many people to split the bill? "))

total = total * (1 + percent/100)
split = round(total/split, 2)

print(f"Each person should pay: ${split}")
