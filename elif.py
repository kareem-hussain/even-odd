weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

bmi = weight / (height ** 2)

print("Your BMI is:", round(bmi, 2))
if bmi < 18:
    print("you are underweight")
elif bmi > 18:
    print("you are bmi is normal")
elif bmi > 24:
    print("you are overweight")
elif bmi >30:
    print("obesity")            




   