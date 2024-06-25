# Day 4 - Control Flow and Logical Operators ⚡

## Topics 📃
- **Conditional Statements**
- **Logical Operators**
- **Code Blocks**
- **Scope**

# Auditorium Exercise 🌠

## **8. Odd or Even**

Write a program that works out whether if a given number is an odd or even number.

```python
number = int(input())
if number % 2 == 0:
  print("This is an even number.")
else:
  print("This is an odd number.")
```

## **9. BMI 2.0**

Create an advanced version of BMI calculator you made in Exercise 6. The calculator should also tell the interpretation of the BMI based on the BMI value.
 
```python
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
```
  
## **10. Leap Year**

Write a program that works out whether if a given year is a leap year or not. Before writing the program, make your familiar with the condition when a year is considered leap.

```python
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
```

# Project - Treasure Island 🚀

Create a text-based adventure game where the player navigates through a series of choices to find the hidden treasure.

```python
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

direction = input('You are at a cross road. Where do you want to go? Type "left" or "right"\n').lower()
if direction == "left":
          decision = input('Now you are at a lake. What do you want to do? Type "swim" or "wait"\n').lower()
          if decision == 'wait':
                    door = input('Now you have three doors in front of you. Which one will you go through? "blue", "yellow", or "red"\n').lower()
                    if door == "yellow":
                              print("You win.")
                    elif door == "red":
                              print("Burned by fire. Game over")
                    elif door == "blue":
                              print("Eaten by beasts. Game over")
                    else:
                              print("Game over")                              
          else:
                    print("Attacked by trout. Game over")
                    
else:
          print("You fall into a hole. Game over")

