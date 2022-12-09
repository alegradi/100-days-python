# BMI calculator II
# Calculate BMI and tell them the interpretation

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = weight / (height ** 2)

# formatted_bmi = "{:.2f}".format(bmi)
# print(formatted_bmi)

rounded_bmi = round(bmi)

if rounded_bmi <= 18.5:
    print(f"Your BMI is {rounded_bmi}, you are underweight.")
elif rounded_bmi <= 25:
    print(f"Your BMI is {rounded_bmi}, you have normal weight.")
elif rounded_bmi <= 30:
    print(f"Your BMI is {rounded_bmi}, you are slightly overweight.")
elif rounded_bmi <= 35:
    print(f"Your BMI is {rounded_bmi}, you are obese.")
else:
    print(f"Your BMI is {rounded_bmi}, you are clinically obese.")
