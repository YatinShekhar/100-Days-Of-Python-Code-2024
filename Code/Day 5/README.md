# Day 5 - Python Loops ⚡

## Topics 📃
- **For loops**
- **Range**
- **Code Blocks**

# Auditorium Exercise 🌌

## 16. Average Height

Write a program that calculates the average student height from a list of heights without using `sum()` or `len()` function.

```python
student_heights = input('Enter the height(in cm): ').split()

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

total_height = 0
for height in student_heights:
    total_height += height

print(f"total height = {total_height} cm")

students = 0
for n in student_heights:
    students += 1

print(f"number of students = {students}")

average_height = round(total_height / students)

print(f"average height = {average_height} cm")
```

## 17. High Score

Write a program that calculates the highest score from a list of scores without using `min()` or `max()` function.

```python
student_scores = input("Enter the student's score: ").split()

for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score

print(f"The highest score in the class is: {highest_score}")
```

## 18. Adding Even Numbers

Write a program that calculates the sum of all the even numbers from 1 to X. If X is 100 then the first even number would be 2 and the last one is 100.
Important, there should only be 1 print statement in your console output.

```python
target = int(input('Enter the number: '))

sum = 0
for n in range(0, target + 1, 2):
    sum += n

print(sum)
```

## 19. FizzBuzz

Write a program that automatically prints the solution to the FizzBuzz game. These are the rules of the FizzBuzz game:

- When the number is divisible by 3 then instead of printing the number it should print "Fizz".
- When the number is divisible by 5, then instead of printing the number it should print "Buzz".`
- And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"

```python
for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
```

# Project - PyPassword Generator 🚀

Write a program which creates a password consisting of letters, numbers and symbols in a random order. Create two level in this program
- **1. Easy Level:** Order not randomised
- **2. Hard Level:** Order of characters randomised

```python
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

random_letters = []
for n in range(0,nr_letters):
    a = random.randint(0, len(letters) - 1)
    random_letters.append(letters[a])

random_symbols = []
for n in range(0,nr_symbols):
    a = random.randint(0, len(symbols) - 1)
    random_symbols.append(symbols[a])

random_numbers = []
for n in range(0,nr_numbers):
    a = random.randint(0, len(numbers) - 1)
    random_numbers.append(numbers[a])

random_password = random_letters + random_symbols + random_numbers
```
Till this point, the code for both the level is same. And now we will be writing code for both the level which would be slightly different

### **Easy level:**
```python
easy_password = ''
for n in random_password:
    easy_password = easy_password + n
print(f"Easy password: {easy_password}")
```

### **Hard level:**
```python
hard_password = ''
random.shuffle(random_password)
for n in random_password:
    hard_password = hard_password + n
print(f"Hard password: {hard_password}")
```



