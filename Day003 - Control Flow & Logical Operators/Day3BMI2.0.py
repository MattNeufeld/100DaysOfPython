height = float(input("Please enter your height: "))
weight = float(input("Please enter your weight: "))

bmi = round(weight / (height ** 2))

if(bmi <18.5):
    print(f"You have a BMI of {bmi} which is underweight")
elif(bmi >= 18.5 and bmi < 25):
    print(f"You have a BMI of {bmi} which is a normal weight")
elif(bmi >= 25 and bmi < 30):
    print(f"You have a BMI of {bmi} which is overweight")
elif(bmi >= 30 and bmi < 35):
    print(f"You have a BMI of {bmi} which is obese")
else:
    print(f"You have a BMI of {bmi} which is clinically obese")
    

