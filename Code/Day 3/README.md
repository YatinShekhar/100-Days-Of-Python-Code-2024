# Day 3 - Control Flow and Logical Operators ⚡

## Topics 📃
- **Conditional Statements**
- **Logical Operators**
- **Code Blocks**
- **Scope**

# Auditorium Exercise 🌠

## **8. Odd or Even**

Write a program that works out whether if a given number is an odd or even number.

```python
number = int(input('Enter the number: '))

if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")
```

## **9. BMI 2.0**

Create an advanced version of BMI calculator you made in Exercise 6. The calculator should also tell the interpretation of the BMI based on the BMI value.
 
```python
height = float(input('Enter the height(in metre): '))
weight = int(input('Enter the weight(in kg): '))

BMI = round(weight / height ** 2, 2)

if BMI < 18.5:
    print(f"Your BMI is {BMI}, you are underweight.")
elif 18.5 <= BMI < 25:
    print(f"Your BMI is {BMI}, you have a normal weight.")
elif 25 <= BMI < 30:
    print(f"Your BMI is {BMI}, you are slightly overweight.")
elif 30 <= BMI < 35:
    print(f"Your BMI is {BMI}, you are obese.")
else:
    print(f"Your BMI is {BMI}, you are clinically obese.")
```
  
## **10. Leap Year**

Write a program that works out whether if a given year is a leap year or not. Before writing the program, make yourself familiar with the condition when a year is considered leap.

```python
year = int(input('Enter the year: '))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not a leap year")
    else:
        print("Leap year")
else:
    print("Not a leap year")
```

## **11. Pizza Order Practice**

Write a program that creates a final bill for the user on the basis of their order.

```python
print("Thank you for choosing Python Pizza Deliveries!")

size = input('What size pizza do you want? S, M, or L')
add_pepperoni = input('Do you want pepperoni? Y or N')
extra_cheese = input('Do you want extra cheese? Y or N')

if size == 'S':
    bill = 15
elif size == 'M':
    bill = 20
else:
    bill = 25

if add_pepperoni == 'Y':
    if size == 'S':
        bill += 2
    else:
        bill += 3

if extra_cheese == 'Y':
    bill += 1

print(f"Your final bill is: ${bill}.")
```

## **12. Love Calculator**

Write a program that tests the compatibility between two people bases on their names and returns the score.

```python
name1 = input('Enter the first name: ') 
name2 = input('Enter the second name: ')

combined_name = name1.upper() + name2.upper()

T = combined_name.count("T") 
R = combined_name.count("R")
U = combined_name.count("U")
E = combined_name.count("E")
total_true_count = T + R + U + E

L = combined_name.count("L")
O = combined_name.count("O")
V = combined_name.count("V")
E = combined_name.count("E")
total_love_count = L + O + V + E

love_score = int(str(total_true_count) + str(total_love_count))
your_score = f"Your score is {love_score}"

if love_score < 10 or love_score > 90:
    print(f"{your_score}, you go together like coke and mentos.")
elif 40 < love_score < 50:
    print(f"{your_score}, you are alright together.")
else:
    print(f"{your_score}.")
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

