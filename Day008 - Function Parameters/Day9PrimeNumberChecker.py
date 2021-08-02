def prime_checker(number):
    p = True
    for i in range(2,number):
        if number % i == 0:
            p = False
    if p:
        print("The number is prime")
    else:
        print("The number is not prime")



n = int(input("Check this number: "))
prime_checker(number=n)
