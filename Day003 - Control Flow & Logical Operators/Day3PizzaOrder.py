print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

total = 0
if(size == "S"):
    total = total + 15
    if(add_pepperoni == "Y"):
        total = total + 2
elif(size == "M"):
    total = total + 20
    if(add_pepperoni == "Y"):
        total = total + 3
else:
    total = total + 25
    if(add_pepperoni == "Y"):
        total = total + 3
if(extra_cheese == "Y"):
    total = total + 1
print(f"Your final bill is: ${total}.")
