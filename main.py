# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi = round(weight / height ** 2)
if bmi < 18.5:
  print(f"Your bmi is {bmi}, you are underweight.")
elif bmi < 25:
  print(f"Your bmi is {bmi}, You have a normal weight.")




