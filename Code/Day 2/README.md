# Day 2 - Understanding Data Types and How to Manipulate Strings ⚡

## Topics 📃
- **Datatypes**
- **Numbers**
- **Operations**
- **Type Conversion**
- **f-Strings**

# Auditorium Exercise 🌀

## **5. Data Types**

Write a program that adds the digits in a 2 digit number

```python
two_digit_number = input('Enter a two-digit number: ')

sum = int(two_digit_number[0]) + int(two_digit_number[1])
print(f'The sum of digit is: {sum}')
```

## **6. BMI Calculator**

Write a program that calculates the Body Mass Index (BMI) from a user's weight and height

```python
height = input('Enter your height(in metre):' )
weight = input('Enter your weight(in kg):' )

BMI = int(float(weight)/float(height)**2)
print(f'BMI Index: {BMI}')
```

## **7. Life in Weeks**

Create a program using maths that tells us how many weeks we have left, if we live until 90 years old.

```python
age = input('Enter your age: ')

total_weeks = 90 * 52
current_weeks = int(age) * 52

remaining_weeks = total_weeks - current_weeks 
print(f"You have {remaining_weeks} weeks left.")
```


# Project - Tip Calculator 🚀

You and your friends went out for lunch. Write a program that splits the bill equally among each friend.

```python
print("Welcome to the tip calculator!")

total_bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

final_bill = round((total_bill + total_bill * (tip/100))/people, 2)
print(f"Each person should pay: ${final_bill}")
```
