

def add(n1, n2):
    return n1 + n2
def sub(n1, n2):
    return n1 - n2
def mult(n1, n2):
    return n1 * n2
def div(n1, n2):
    return n1 * n2

end = False
cont = False
first = 0
while not end:
    if  not cont:
        first = float(input("What's the first number?: "))
    print("+\n-\n*\n/\n")
    op = input("Pick an operation: ")
    second = float(input("What's the next number?: "))
    if(op == "+"):
        result = add(first, second)
    elif(op == "-"):
        result = sub(first, second)
    elif(op == "*"):
        result = mult(first, second)
    else:
        result = div(first, second)
    print(f"{first} {op} {second} = {result}")
    inp = input(f"Type 'y' to continue calculating with {result}, type 'n' to start a new calculation, type 'x' to exit: ")
    if inp == "y":
        cont = True
        first = result
    elif inp == "n":
        cont = False
    else:
        end = True
