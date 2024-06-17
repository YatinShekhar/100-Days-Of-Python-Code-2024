# 8. Odd or Even

number = int(input())
if number % 2 == 0:
  print("This is an even number.")
else:
  print("This is an odd number.")
  

# 9. BMI 2.0

height = float(input())
weight = int(input())
bmi = weight / height ** 2
if bmi < 18.5:
  print(f"Your BMI is {bmi}, you are underweight.")
elif bmi >= 18.5 and bmi < 25:
  print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi >= 25 and bmi < 30:
  print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi >= 30 and bmi < 35:
  print(f"Your BMI is {bmi}, you are obese.")
else:
  print(f"Your BMI is {bmi}, you are clinically obese.")


# 10. Leap Year

year = int(input())
if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year")
    else:
      print("Not leap year")
  else:
    print("Leap year")
else:
    print("Not leap year")
